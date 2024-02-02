from django.shortcuts import render,get_object_or_404
from .models import Item

def details(request, pk):
    item = get_object_or_404(Item, id = pk)
    
    return render(request, 'item/detail.html', {
        'item' : item
    })