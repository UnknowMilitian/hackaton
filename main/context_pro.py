from .models import *

def view_all(request):
    context = {
        'category':Category.objects.all(),
        'turnirs':Turnir.objects.all().order_by('-id')[:3],
        'tadbirs':Tadbir.objects.all().order_by('-id')[:3]
    }
    return context