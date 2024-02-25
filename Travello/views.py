from django.shortcuts import render,redirect
from .models import Destination
# Create your views here.
def index(request):
    
    dests = Destination.objects.all()
    
    return render(request,'index.html',{'dests':dests})

def filter(request):
    filt = Destination.objects.all()
    if request.method == 'GET':
        city = request.GET['city']
        price = request.GET['price']
        if city != None or price != None:
            filt=Destination.objects.filter(price=filt)
            filt=Destination.objects.filter(name=filt)
    return redirect (request,'')