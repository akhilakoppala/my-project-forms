from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display_form(request):
    if request.method=="POST":
        un=request.POST['usn']
        pw=request.POST['psw']
        print(un)
        print(pw)
        return HttpResponse('data is submitted')
    
    return render(request,'display_form.html')

