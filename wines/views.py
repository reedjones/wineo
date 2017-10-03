from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .models import Winery, Wine, Note
from .forms import WineForm

def wine_index(request):
    wines = Wine.objects.all().order_by('created_on')
    return render(request, 'wines/index.html', {'wines': wines})


def wine_single(request, pk):
    try:
        wine = Wine.objects.get(pk=pk)
    except Wine.DoesNotExist:
        return Http404

    notes = Note.objects.filter(about=wine)
    return render(request, 'wines/single.html', {'wine': wine, 'notes': notes})


def write_note(request, pk):
    try:
        wine = Wine.objects.get(pk=pk)
    except Wine.DoesNotExist:
        return Http404



def add_wine(request):
    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES)
        if form.is_valid():
            print("valid")
            new_wine = form.save()

            return HttpResponseRedirect(new_wine.get_url())
        else:
            return render(request, 'wines/add.html', {'form':form})
    else:
        return render(request, 'wines/add.html', {})


def delete_wine(request, pk):
    if request.method == 'POST':
        try:
            wine = Wine.objects.get(pk=pk)
            wine.delete()
            return HttpResponse("wine deleted")
        except Wine.DoesNotExist:
            return HttpResponse("invalid wine")

    else:
        try:
            wine = Wine.objects.get(pk=pk)
        except Wine.DoesNotExist:
            return Http404

    return render(request, 'wines/delete.html', {'wine': wine})


def edit_wine(request, pk):
    if request.method == 'POST':
        try:
            wine = Wine.objects.get(pk=pk)
            wine.delete()
            return HttpResponse("wine deleted")
        except Wine.DoesNotExist:
            return HttpResponse("invalid wine")

    else:
        try:
            wine = Wine.objects.get(pk=pk)
        except Wine.DoesNotExist:
            return Http404

    return render(request, 'wines/edit.html', {'wine': wine})

