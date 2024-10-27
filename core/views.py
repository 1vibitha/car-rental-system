from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from item.models import Category, Item
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import EditProfileForm, CustomPasswordChangeForm
from django.contrib.auth import logout as auth_logout

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories' : categories,
        'items' : items
    })
def category(request):
    
    return render(request, 'core/category.html')

def contact(request):
    return render(request, 'core/contact.html')


def ask_login(request):
    action = request.GET.get('action', '')  # Get the action parameter from the URL
    message = "Welcome! You need to log in to contact the seller." if action == "contact" else "Welcome! You need to log in to book the car."

    return render(request, 'core/ask_login.html', {'message': message})

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

@login_required  # Ensure the user is logged in
def log(request):
    items = Item.objects.all()# Get a few items for display
    categories = Category.objects.all()
    filter_item = Item.objects.exclude(created_by=request.user)
    

    # Calculate the count of items per category that are not created by the logged-in user
    for category in categories:
        category.item_count = category.items.exclude(created_by=request.user).count()


    return render(request, 'core/index2.html', {
        'categories': categories,
        'items': items,
        'filter_item': filter_item
    })

def logout(request):
    auth_logout(request)
    return redirect('core:index') 

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('log')  # Redirect to index2.html or your logged-in page
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'core/login.html')  # Show the login form if not POST
def about(request):
    return render(request, 'core/about.html')

def car(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/cars.html', {
        'categories' : categories,
        'items' : items
    })


def feature(request):
    return render(request, 'core/feature.html')

def service(request):
    return render(request, 'core/service.html')

def test(request):
    return render(request, 'core/testimonial.html')

#To edit profile

@login_required
def edit_profile(request):
    profile_form = None
    if request.method == 'POST':
        # Handle profile update
        profile_form = EditProfileForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('core:log')  # Redirect to the appropriate page after successful update

    else:
        profile_form = EditProfileForm(instance=request.user)

    return render(request, 'core/profile.html', {
        'profile_form': profile_form
    })


@login_required
def change_password(request):
    password_form = None
    if request.method == 'POST':
        # Handle password change
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Prevent logout after password change
            messages.success(request, 'Your password was successfully updated!')
            return redirect('core:log')  # Redirect to the appropriate page after successful password change

    else:
        password_form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'core/password.html', {
        'password_form': password_form
    })

