from django.shortcuts import render, redirect
from .models import Contacts
from .forms import MessageFromCustomerForm, SubscriberForm




def index(request):
    if request.method == 'POST':
        form = MessageFromCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')

        context = {
            'message_form': form,
            'contacts': Contacts.objects.first()
        }
        return render(request, 'contacts.html', context=context)
    else:
        context = {
            'message_form': MessageFromCustomerForm(),
            'contacts': Contacts.objects.first()
        }
        return render(request, 'contacts.html', context=context)






def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:subscribe')
    else:
        form = SubscriberForm()

    return render(request, 'contacts.html', {'form': form})


