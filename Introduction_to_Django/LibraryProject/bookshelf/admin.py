from django.contrib import admin
from .models import Book

# Customize admin display for Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display
    search_fields = ('title', 'author')                      # Search by title or author
    list_filter = ('publication_year',)                      # Filter by publication year

# Register Book model with admin
admin.site.register(Book, BookAdmin)