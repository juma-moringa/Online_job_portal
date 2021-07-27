from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import ClientRegistrationForm, EmployerRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def index(request):
    return render(request,'index.html')

class client_register(CreateView):
    model = User
    form_class = ClientRegistrationForm
    template_name='client_register.html'

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('login')

class employer_register(CreateView):
    model = User
    form_class = EmployerRegistrationForm
    template_name='employer_register.html'

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('login')      

@csrf_exempt
def login_request(request):
    if request.method =='POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                return redirect('landingpage')
            else:
                messages.error(request,"Invalid username or password") 
        else:
                messages.error(request,"Invalid username or password")       
    return render(request,'login.html',{'form':AuthenticationForm})        

def logout_request(request):
    logout(request)
    return redirect('login')
    
def landingpage(request):
    return render(request,"landingpage.html")
       

