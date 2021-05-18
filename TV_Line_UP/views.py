from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    return redirect('/shows')
    
def shows(request):
    context ={
        'Shows_Db':TV_Shows.objects.all()
    }
    return render(request, 'index.html', context)

def add_form(request):
    return render(request, 'add.html')

def edit_form(request, val):
    context ={
        'the_show':TV_Shows.objects.get(id=val)
    }
    return render(request, 'edit.html', context)

def details(request,val):
    context ={
        'the_show':TV_Shows.objects.get(id=val)
    }
    return render(request, 'details.html', context)

def delete(request, val):
    this_show= TV_Shows.objects.get(id=val)
    this_show.delete()
    return redirect('/shows')

def adding(request):
    errors=TV_Shows.objects.base_valid(request.POST)
    if len(errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/add')
    else:
        TV_Shows.objects.create(
            title=request.POST['title_input'],
            network=request.POST['network_input'],
            release_date=request.POST['Rd_date_input'],
            description=request.POST['desc_input'],
        )
    this_show = TV_Shows.objects.last()
    return redirect(f'/shows/details/{this_show.id}')

def editing(request, val):
    this_show = TV_Shows.objects.get(id=val)
    errors = TV_Shows.objects.base_valid(request.POST)
    if len(errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/edit/{this_show.id}')
    else:
        if request.POST["title_input"] != "":
            this_show.title=request.POST['title_input']
            this_show.save()
        if request.POST["network_input"] != "":
            this_show.network=request.POST['network_input']
            this_show.save()
        if request.POST["Rd_date_input"] != "":
            this_show.release_date = request.POST['Rd_date_input']
            this_show.save()
        if request.POST["desc_input"] != "":
            this_show.description=request.POST['desc_input']
            this_show.save()
    return redirect(f'/shows/details/{this_show.id}')