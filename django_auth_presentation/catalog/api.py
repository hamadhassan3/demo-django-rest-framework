from catalog.models import Book
from rest_framework import viewsets
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """This viewset provides create, retrieve, update and delete apis for books"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
