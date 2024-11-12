
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import BookingForm, PaymentForm 
from item.models import Item
from django.contrib.auth.decorators import login_required
from .models import Booking
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking, Item


@login_required
def rented_items(request):
    # Only get active bookings for the user
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

        return redirect('booking:rented_items')  # Redirect to refresh the page

    return render(request, 'booking/rented_items.html', {
        'bookings': bookings,
    })


@login_required
def book_car(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Temporarily store form data in session to use after payment completion
            request.session['booking_data'] = form.cleaned_data
            request.session['item_id'] = item_id  # Store item ID for payment confirmation

            # Redirect to payment page
            return redirect('booking:payment')
    else:
        form = BookingForm()

    return render(request, 'booking/booking.html', {
        'form': form,
        'item': item
    })

@login_required
def payment(request):
    booking_data = request.session.get('booking_data')
    item_id = request.session.get('item_id')
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment_method = payment_form.cleaned_data['payment_method']
            if (payment_method == 'card' and all(payment_form.cleaned_data.get(field) for field in ['card_number', 'card_name', 'cvv', 'expiry_date'])) or \
               (payment_method == 'upi' and payment_form.cleaned_data.get('upi_id')):

                booking = Booking.objects.create(
                    item=item,
                    user=request.user,
                    **booking_data
                )
                item.is_sold = True
                item.save()

                subject = f'Car Booking Confirmation for {item.name}'
                message = f"""
                Dear {booking_data['name']},

                Thank you for booking {item.name}!

                Here are your booking details:
                - Name: {booking_data['name']}
                - Email: {booking_data['email']}
                - Phone: {booking_data['phone']}
                - Address: {booking_data['address']}
                - Pincode: {booking_data['pincode']}

                The car will be delivered to the provided address.

                Thank you for choosing us!

                Best Regards,
                Your Car Rental Service
                """
                from_email = settings.DEFAULT_FROM_EMAIL
                send_mail(subject, message, from_email, [booking_data['email']])

                del request.session['booking_data']
                del request.session['item_id']
                return redirect('booking:success')
            else:
                payment_form.add_error(None, "Please fill in all required payment details.")
    else:
        payment_form = PaymentForm()

    return render(request, 'booking/payment.html', {
        'payment_form': payment_form,
        'item': item
    })

def booking_success(request):
    return render(request, 'booking/success.html')
