from django.urls import path
from .views import *


urlpatterns = [
    path('',index),
    path('about',about, name='about'),
    path('service',services, name='service'),
    path('menu',menu, name='menu'),
    path('reservation',reservation),
    path('testimonial',testimonials),
    path('contact',contact),



    path('register/', register),
    path('userlogin/',userLogin),
    path('userlogout/',userLogout)  



]
