from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def trial(request):
    return HttpResponse("<h1>Project is on air</h1>")

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"yoke/home.html")

def profile(request):
    name="Yokesh"
    return render(request,"yoke/profile.html",{'name':name})