from django.urls import path
from .views import register, user_profile, update_profile, forgot_password, reset_password
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('register/', register, name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', user_profile, name='user_profile'),
    path('profile/update/', update_profile, name='update_profile'),
    path('forgot-password/', forgot_password, name='forgot_password'),
]
path('reset-password/', reset_password, name='reset_password'),
