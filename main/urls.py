from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', home, name='home'),
    path('Биз ҳақимизда/', about, name='about'),
    path('Маҳсулот/', servicer, name='servicer'),
    path('Галлерй/', gallery, name='gallery'),
    path('Контак/ ', contact, name='contact'),
    path('Янглик/', news, name='news'),

]
