from django.urls import path, include
from main.views import *
# from main.views import About

urlpatterns = [
    path('', home, name='home'),
    path('Биз ҳақимизда/', about,  name='about'),
    # path('Биз ҳақимизда/', About.as_view(), name='about'),
    path('Маҳсулот/', servicer, name='servicer'),
    path('Галлерй/', gallery, name='gallery'),
    path('Контак/ ', contact, name='contact'),
    path('Янглик/', news, name='news'),
    path('venue_pdf/<int:pk>', venue_pdf, name='venue_pdf')

]
