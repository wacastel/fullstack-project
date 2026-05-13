from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse

API_URL = "http://127.0.0.1:8000/items/"

def item_list(request):
    # READ
    response = requests.get(API_URL)
    items = response.json()
    return render(request, 'items/list.html', {'items': items})

def item_create(request):
    # CREATE
    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "description": request.POST.get("description")
        }
        requests.post(API_URL, json=data)
        return redirect('item_list')
    return render(request, 'items/form.html')

def item_update(request, pk):
    # UPDATE
    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "description": request.POST.get("description")
        }
        requests.put(f"{API_URL}{pk}", json=data)
        return redirect('item_list')
    
    response = requests.get(f"{API_URL}{pk}")
    return render(request, 'items/form.html', {'item': response.json()})

def item_delete(request, pk):
    # DELETE
    if request.method == "POST":
        requests.delete(f"{API_URL}{pk}")
        return redirect('item_list')
    return render(request, 'items/confirm_delete.html', {'pk': pk})
