from django.shortcuts import render
from page import views

# Create your views here.
def home(request):
    return render(request,'home.html',{'home':home})

# 1번 공통문항
def main(request):
    return render(request,'main.html',{'main':main})

# 2~4번 바다
def sea1(request):
    return render(request,'sea1.html',{'sea1':sea1})

def sea2(request):
    return render(request,'sea2.html',{'sea2':sea2})

def sea3(request):
    return render(request,'sea3.html',{'sea3':sea3})

# 2~4번 산
def mountain1(request):
    return render(request,'mountain1.html',{'mountain1':mountain1})

def mountain2(request):
    return render(request,'mountain2.html',{'mountain2':mountain2})

def mountain3(request):
    return render(request,'mountain3.html',{'mountain3':mountain3})

# 2~4번 사막
def desert1(request):
    return render(request,'desert1.html',{'desert1':desert1})

def desert2(request):
    return render(request,'desert2.html',{'desert2':desert2})

def desert3(request):
    return render(request,'desert3.html',{'desert3':desert3})

# 영화 결과 페이지
def act(request):
    return render(request,'act.html',{'act':act})    

def ani(request):
    return render(request,'ani.html',{'ani':ani})    

def com(request):
    return render(request,'com.html',{'com':com})    

def hor(request):
    return render(request,'hor.html',{'hor':hor})    

def rom(request):
    return render(request,'rom.html',{'rom':rom})    