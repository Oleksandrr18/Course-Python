from django.shortcuts import render
from menu.models import Category


# Create your views here.
def index(request):
    categories = Category.objects.filter(is_visible=True)
    context = {
        'categories': categories,
    }
    return render(request, 'services.html', context=context)