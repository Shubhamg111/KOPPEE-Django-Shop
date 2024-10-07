from .models import *

def setting(request):
    context={
        'setting':Setting.objects.last()
    }
    return context