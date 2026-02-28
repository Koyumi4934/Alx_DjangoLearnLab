from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# --- Function-based view to list all books ---
def list_books(request):
    books = Book.objects.all()  # ALX expects this exact query
    return render(request, 'relationship_app/list_books.html', {'books': books})

# --- Class-based view to show a library and its books ---
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # Pass as 'library' to template

# --- User registration view ---
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # Redirect after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})