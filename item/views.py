from django.shortcuts import render, get_object_or_404, redirect
from . models import Item, Category
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm,EditItemForm
from django.db.models import Q

# Create your views here.
from django.db.models import Q

def items(request):
    query = request.GET.get('query', '')  # Search query
    category_id = request.GET.get('category', 0)  # Category filter
    seats = request.GET.get('seats', '')  # Seat filter (as a string)
    items = Item.objects.filter(is_sold=False)  # Only get available items
    categories = Category.objects.all()  # All categories

    # Filter by category if selected
    if category_id and category_id != '0':
        items = items.filter(category_id=category_id)

    # Filter by query (searching by name, company, model, or category)
    if query:
        items = items.filter(
            Q(name__icontains=query) |
            Q(company__icontains=query) |
            Q(model__icontains=query) |
            Q(category__name__iexact=query)
        )

    # Filter by seat number if provided and it's a valid digit
    if seats.isdigit():
        items = items.filter(seats=int(seats))  # Correct field is `seats`

    # Render the template with the filtered items and form values
    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
        'seats': seats,  # Pass the seats back to the template
    })




def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items':related_items
    })


@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            # Check if the user added a new category
            new_category_name = form.cleaned_data.get('new_category')
            if new_category_name:
                # Check if a category with the same name already exists
                category, created = Category.objects.get_or_create(name=new_category_name)
            else:
                # Use the existing category
                category = form.cleaned_data.get('category')

            # Create the item
            item = form.save(commit=False)
            item.created_by = request.user
            item.category = category  # Assign the selected or new category
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'title': 'Add New Item',
        'form': form
    })

@login_required
def delete(request,pk):
    item=get_object_or_404(Item,pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

@login_required
def edit(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'title': 'Edit Item',
        'form': form
    })
