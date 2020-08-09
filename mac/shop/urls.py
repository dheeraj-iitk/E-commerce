from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="shophome"),
    path('contact/',views.contact,name="contactus"),
    path('about/',views.about,name="aboutus"),
    path('tracker/',views.tracker,name="tracking"),
    path('product/<int:myid>',views.prodview,name="product"),
    path('search/',views.search,name="search"),
    path('checkout/',views.checkout,name="checkout"), 
]