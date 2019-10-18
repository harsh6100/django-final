from django.shortcuts import render,redirect
from .forms import SignupForm
import requests
import json


def LogIn(request):
    return render(request,'account/home.html')

def SignUp(request):
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            data1=json.dumps(form)
            headers={'content-type': 'application/json'}
            url='http://127.0.0.1:8000/api/account/register'
            requests.post(url,headers=headers,data=data1)
            # return redirect()
    else:
        form = SignupForm()
        return render(request,'account/register.html',{'form':form})
            
