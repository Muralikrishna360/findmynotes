from django_filters import FilterSet

from app.models import Book


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = ['college', 'department', 'subject', 'topic']