from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('servicer/', servicer, name='servicer'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact'),
    path('news/', news, name='news'),

]