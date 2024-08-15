from .models import Contacts


def contacts(request):
    return {
        'index_contacts': Contacts.objects.first()
    }