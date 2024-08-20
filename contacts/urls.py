from django.urls import path
from .views import index
from .views import subscribe

app_name = 'contacts'



urlpatterns = [
    path('', index, name='index'),
    path('subscribe/', subscribe, name='subscribe'),
]