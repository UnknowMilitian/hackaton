from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.views.generic import (
	TemplateView,
	ListView,
    CreateView,
	DetailView,
	View
)
# Create your views here.

def homePage(request):
    if request.method == 'POST':
        cont = ContactForm(request.POST)
        if cont.is_valid():
            c = cont.save(commit=False)
            c.save()
            return HttpResponseRedirect(request.path)
    else:
        cont = ContactForm()
    context = {
        'cont':cont,
        'turnirs':Turnir.objects.all(),
    }
    return render(request, 'index.html', context)


def turnir_detail(request, pk):
    turnir = Turnir.objects.get(id=pk)
    if request.method == 'POST':
        form = TurnirQuestionForm(request.POST)
        auth = TurnirAuthForm(request.POST)
        if auth.is_valid():
            a = auth.save(commit=False)
            a.turnir = turnir
            a.save()
            return HttpResponseRedirect(request.path)

        if form.is_valid():
            f = form.save(commit=False)
            f.turnir = turnir
            f.save()
            return HttpResponseRedirect(request.path)
    else:
        auth = TurnirAuthForm()
        form = TurnirQuestionForm()
    context = {
        'turnir':turnir,
        'auth':auth,
        'form':form,
    }
    return render(request, 'detail.html', context)

def tadbir_detail(request, pk):
    tadbir = Tadbir.objects.get(id=pk)
    if request.method == 'POST':
        form = TurnirQuestionForm(request.POST)
        auth = TurnirAuthForm(request.POST)
        if auth.is_valid():
            a = auth.save(commit=False)
            a.tadbir = tadbir
            a.save()
            return HttpResponseRedirect(request.path)

        if form.is_valid():
            f = form.save(commit=False)
            f.tadbir = tadbir
            f.save()
            return HttpResponseRedirect(request.path)
    else:
        auth = TurnirAuthForm()
        form = TurnirQuestionForm()
    context = {
        'tadbir':tadbir,
        'auth':auth,
        'form':form,
    }
    return render(request, 'tadbir-detail.html', context)

# class ContactCreateView(CreateView):
#     model = TurnirQuestion
#     fields = ['name_surname', 'age', 'telephone', 'text']
#     template_name = 'index.html'
#     success_url = '/'