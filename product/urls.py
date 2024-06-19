from django.urls import path
from .views import product_list, create_product, product_detail, update_product, delete_product, create_review, get_reviews, delete_review

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/create/', create_product, name='create_product'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/<int:pk>/update/', update_product, name='update_product'),
    path('products/<int:pk>/delete/', delete_product, name='delete_product'),
    path('products/<int:pk>/reviews/', create_review, name='create_review'),
    path('products/<int:pk>/reviews/get/', get_reviews, name='get_reviews'),
    path('products/<int:pk>/reviews/<int:review_id>/delete/', delete_review, name='delete_review'),  # Add this line
]
