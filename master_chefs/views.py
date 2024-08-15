from django.shortcuts import render
from .models import Staff


# Create your views here.
def index(request):
    staff = Staff.objects.filter(is_visible=True).order_by('sort')
    context = {
        'staff': staff
    }
    return render(request, 'masters.html', context=context)