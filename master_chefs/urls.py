from django.urls import path
from .views import index

app_name = 'masters'

urlpatterns = [
    path('', index, name='index'),
]