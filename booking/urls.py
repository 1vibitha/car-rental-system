from django.urls import path

from . import views


app_name='booking'


urlpatterns = [
    path('booking/<int:item_id>/', views.book_car, name='book_car'),
    path('rented-items/', views.rented_items, name='rented_items'),
]
