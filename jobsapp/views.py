from django.shortcuts import render
from django.views.generic import CreateView
from .models import Candidates, Company, NewsLetterRecipients, User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import AddjobForm, ClientRegistrationForm, EmployerRegistrationForm, JobApplicationForm, NewsLetterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse




# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'aboutus.html')
def landingpage(request):
    return render(request,"landingpage.html")
    
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
    
     #application form 
@login_required(login_url='/accounts/login/') 
def applyLinkup(request):
    if request.method=='POST':
        form=JobApplicationForm(request.POST,request.FILES)
        if  form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobApplicationForm()        
    return render(request,'applyjob.html',{'form':form})

@login_required(login_url='/accounts/login/') 
def addjob(request):
    if request.method=='POST':
        form=AddjobForm(request.POST,request.FILES)
        if  form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddjobForm()        
    return render(request,'addjob.html',{'form':form})

def home(request):
    if request.user.is_authenticated and request.user.is_employer:
        candidates=Candidates.objects.filter(company__name=request.user.username)
        candidate = Candidates.objects.all()
        return render(request,'All_applicants.html',{'candidates':candidates,'applicants':candidate})
    else:
        jobs=Company.objects.all()
        return render(request,'All_jobs.html',{'jobs':jobs,})

@login_required(login_url='/accounts/login/')
def search_job(request):
    if 'position' in request.GET and request.GET["position"]:
        search_term = request.GET.get("position")
        found_job = Company.search_by_position(search_term)
        message = f"{search_term}"
        return render(request,'search.html',{"found_job":found_job,"message":message})
    else:
        message = "No matches found"
        return render(request, 'search.html',{"message":message})

#ajax code
def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')
    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to our weekly mailing list'}
    return JsonResponse(data)


def news_today(request):
   
    form = NewsLetterForm()
    return render(request, 'today-news.html', {"letterForm":form})
    