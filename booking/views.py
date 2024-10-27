

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import BookingForm
from item.models import Item
from django.contrib.auth.decorators import login_required
from .models import Booking
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking, Item

@login_required
def rented_items(request):
    bookings = Booking.objects.filter(user=request.user, is_active=True).select_related('item')

    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        booking.is_active = False  # Mark booking as inactive
        booking.save()
        
        # Reset the is_sold status of the item
        item = booking.item
        item.is_sold = False
        item.save()

        return redirect('booking:rented_items')  # Redirect to the same page to see updates

    return render(request, 'booking/rented_items.html', {
        'bookings': bookings,
    })

# views.py
from .models import Booking
from django.shortcuts import get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings

@login_required
def book_car(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # Use get_object_or_404 for better error handling

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Capture the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            pincode = form.cleaned_data['pincode']

            # Create a booking instance
            booking = Booking.objects.create(
                item=item,
                user=request.user,
                name=name,
                email=email,
                phone=phone,
                address=address,
                pincode=pincode
            )

            # Set item as sold
            item.is_sold = True
            item.save()  # Save to update is_sold status in the database

            # Send confirmation email
            subject = f'Car Booking Confirmation for {item.name}'
            message = f"""
            Dear {name},

            Thank you for booking {item.name}!

            Here are your booking details:
            - Name: {name}
            - Email: {email}
            - Phone: {phone}
            - Address: {address}
            - Pincode: {pincode}

            The car will be delivered to the provided address.

            Thank you for choosing us!

            Best Regards,
            Your Car Rental Service
            """
            from_email = settings.DEFAULT_FROM_EMAIL
            send_mail(subject, message, from_email, [email])

            # Redirect to a success page or rented items page
            return redirect('booking:rented_items')
    else:
        form = BookingForm()

    return render(request, 'booking/booking.html', {
        'form': form,
        'item': item
    })
