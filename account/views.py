from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer
from datetime import datetime, timedelta

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    if request.method == 'GET':
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    serializer = UserSerializer(user, data=request.data, partial=True)  # partial=True allows partial updates
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def forgot_password(request):
    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'error': 'User with this email does not exist'}, status=status.HTTP_404_NOT_FOUND)

    token = default_token_generator.make_token(user)
    expire_date = timezone.now() + timedelta(minutes=5)  # Use timezone.now() for timezone-aware datetime
    user.profile.reset_password_token = token
    user.profile.reset_password_expire = expire_date
    user.profile.save()

    link = f"http://127.0.0.1:8000/api/reset_password?token={token}&email={email}"
    message = f"Your Password Reset Link: {link}"
    subject = 'Password Reset Request'
    send_mail(subject, message, 'mrmuhamedabdallah@gmail.com', [user.email])
    return Response({'details': f'password reset link sent to {user.email}'})

@api_view(['POST'])
def reset_password(request):
    token = request.data.get('token')
    email = request.data.get('email')
    new_password = request.data.get('new_password')

    if not token or not email or not new_password:
        return Response({'error': 'Token, email, and new password are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'error': 'User with this email does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if user.profile.reset_password_token != token:
        return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

    if timezone.now() > user.profile.reset_password_expire:
        return Response({'error': 'Token has expired'}, status=status.HTTP_400_BAD_REQUEST)

    user.set_password(new_password)
    user.profile.reset_password_token = None
    user.profile.reset_password_expire = None
    user.profile.save()
    user.save()

    return Response({'details': 'Password has been reset successfully'}, status=status.HTTP_200_OK)
