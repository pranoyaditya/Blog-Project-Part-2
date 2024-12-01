from django.shortcuts import render,redirect
from .forms import RegisterForm

# Create your views here.
def add_author(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('add_author')
    else:
        author_form = AuthorForm()
    return render(request, 'author/add_author.html', {'form' : author_form})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(request, 'author/register.html', {'form' : form})