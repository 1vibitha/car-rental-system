from django.urls import path
app_name='item'
from . import views
urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
   
]