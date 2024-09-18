from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from item.models import Category, Item
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories' : categories,
        'items' : items
    })

def contact(request):
    return render(request, 'core/contact.html')
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {
        'form' : form
    })
def log(request):
    return render(request, 'core/index2.html')
def logout(request):
    return render(request, 'core/index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            # Add error message for invalid login
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')