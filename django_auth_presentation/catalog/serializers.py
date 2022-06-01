from rest_framework import serializers
from catalog.models import Book

class BookSerializer(serializers.ModelSerializer):
    """This class converts model"""

    class Meta:
        model = Book
        fields = '__all__'
