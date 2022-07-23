from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home.as_view(), name="home"),
    path('services/',views.services.as_view(), name="services"),
    path('about/',views.about.as_view(), name="aboutus"),
    path('doctors/',views.doctors.as_view(), name="doctors"),
    path('book/',views.book.as_view(), name="book"),
]
