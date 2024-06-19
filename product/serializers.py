from rest_framework import serializers
from .models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['product', 'user', 'rating', 'comment', 'created_dt']

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # Include reviews for each product

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'brand', 'category', 'ratings', 'stock', 'created_dt', 'user', 'reviews']
