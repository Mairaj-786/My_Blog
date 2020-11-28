from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import user_inform
from .forms import InfoModelForm, UserRegisterForm

# Create your views here.

def index(request):
    form = InfoModelForm()
    return render(request,"index.html",{"form":form})

def contact(request):
        form = InfoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"status":"true"})
        else:
            return JsonResponse({"status":0})
