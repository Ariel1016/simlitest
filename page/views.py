from django.shortcuts import render
from page import views

# Create your views here.
def home(request):
    return render(request,'home.html',{'home':home})

def rom(request):
    return render(request,'rom.html',{'rom':rom})    

