from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse 
from django.views.generic import CreateView
from .models import  Contact

# Create your views here.
def index(request):
    return render(request,'home.html')

def user_login(request):
    if request.method=="POST" :
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user :
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else: return HttpResponse("COMPTE DESACTIVER")
        else: 
            return HttpResponse("Username ou Mot de Passe incorrecte")
    else:
        return render(request,'app_users/login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

class ContactView(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'app_users/contact.html'

  