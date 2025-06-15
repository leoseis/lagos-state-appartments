from django.shortcuts import render, redirect
from .models import Appartment
from .forms import AppartmentForm

# CRUD: Create, Retrieve, Update, Delete, List 

def Appartment_list(request):
    appartments = Appartment.objects.select_related('agent').all()
    context = {
       'appartments': appartments
    }
    return render(request, 'appartments.html', context)

def Appartment_retrieve(request, pk):
    appartment = Appartment.objects.select_related('agent').get(id=pk)
    context = {
       'appartment': appartment
    }
    return render(request, 'appartment.html', context)

def Appartment_create(request):
    form = AppartmentForm() 
    if request.method == 'POST':
        form = AppartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {
        'form': form
    }
    return render(request, 'appartment_create.html', context)

def Appartment_update(request, pk):
    appartment = Appartment.objects.get(id=pk)
    form = AppartmentForm(instance=appartment)

    if request.method == 'POST':
        form = AppartmentForm(request.POST, instance=appartment)
        if form.is_valid():
            form.save() 
            return redirect('/')
    context = {
         'form': form
    }
    return render(request, 'appartment_update.html', context)

def Appartment_delete(request, pk):
    appartment = Appartment.objects.get(id=pk)
    appartment.delete()
    return redirect('/')
