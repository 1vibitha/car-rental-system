
from . import views
from django.contrib.auth import views as auth_views
from . forms import LoginForm
from django.urls import path
from . import views


app_name='core'


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('log/', views.log, name='log'),
    path('logout/', views.logout, name='logout'),
    path('about/', views.about, name='about'),
    path('car/', views.car, name='car'),
    path('feature/', views.feature, name='feature'),
    path('service/', views.service, name='service'),
    path('test/', views.test, name='test'),
    path('profile/', views.edit_profile, name='profile'),
    path('pass/', views.change_password, name='pass'),

    

    

]
