from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect

from project.models import Project
from .forms import UsersForm
from service.models import Service
from news.models import News
from contactenquiry.models import contactEnquiry
from django.core.paginator import Paginator
from django.core.mail import send_mail,EmailMultiAlternatives


#def aboutUS(request):
#   return HttpResponse("WELCOME TO MY PAGE")

def homePage(request):
    #subject='Testing Mail'
    #from_email='xenobaka2@gmail.com'
    #msg='<p>Welcome to <b>My website</b></p>'
    #to='nischal123321@gmail.com'
    #msg=EmailMultiAlternatives(subject,msg,from_email,[to])
    #msg.content_subtype='html'
    #msg.send()
    
    #send_mail(
    #    'Testing Mail',
    #   'Here is the message',
    #   'xenobaka2@gmail.com',
    #    ['nischal123321@gmail.com'],
    #    fail_silently=False,
    #)
    
    newsData=News.objects.all();
    servicesData=Service.objects.all().order_by('-service_title')[:2]#slicing limiting

    #for a in servicesData:
    #    print(a.service_icon)
    #print(services)
    data={
        'servicesData':servicesData,
        'newsData':newsData,
        'title':'Home-Page',
        'name':'Nischal'
    }
    return render(request,"index.html",data)

def newsDetails(request,slug):
    newsDetails=News.objects.get(news_slug=slug)
    data={
        'newsDetails':newsDetails
    }
    return render(request,"newsDetails.html",data)
    

def about(request):
    if request.method=="GET":
        output=request.GET.get('output')
    
    return render(request,"about.html",{'full_name':output})

def services(request):
    servicesData=Service.objects.all().order_by('-service_title')
    
    #paging concept
    
    paginator=Paginator(servicesData,4)
    page_number=request.GET.get('page')
    serviceDatafinal=paginator.get_page(page_number)
    totalpage=serviceDatafinal.paginator.num_pages
    #searching process
    
    if request.method=="GET":
        st=request.GET.get('servicename')
        if st!=None:
           servicesData=Service.objects.filter(service_title__icontains=st)
           
            
    data={
        'servicesData':serviceDatafinal,
        'lastpage':totalpage,
        'totalPagelist':[n+1 for n in range(totalpage)],
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"services.html",data)

def saveEnquiry(request):
    n=''
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        
        en=contactEnquiry(name=name,email=email,phone=phone,message=message)
        en.save()
        n='Data Inserted'
        
        subject='Thanking You'
        from_email='xenobaka2@gmail.com'
        msg='<h1>Welcome to <b>My website</b></h1><p>Thank you for using my website ! I have got your message and I will look for it .<p>'
        to='nischal123321@gmail.com'
        msg=EmailMultiAlternatives(subject,msg,from_email,[to])
        msg.content_subtype='html'
        msg.send()
        
    return render(request,"contact.html")

def contact(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"contact.html",data)

def login(request):
    return render(request,"login.html")

def information_form(request):
    name=0
    data={}
    try:
        if request.method=="POST":
        #n1=(request.GET['num1'])
        #n2=(request.GET['num2'])
          name=request.POST.get('full_name')
          data={
              'full_name':name
          }
          url="/about/?output={}".format(name)
          
          return redirect(url)
    except:
        pass
    
    return render(request,"information_form.html",data)

def form(request):
    fn=UsersForm()
    name=0
    data={'form':fn}
    return render(request,"form.html",data)


def projects(request):
    projectdata=Project.objects.all().order_by('-name')
    
    #paging concept
    
    paginator=Paginator(projectdata,4)
    page_number=request.GET.get('page')
    projectDatafinal=paginator.get_page(page_number)
    totalpage=projectDatafinal.paginator.num_pages
    #searching process
    
    if request.method=="GET":
        st=request.GET.get('-name')
        if st!=None:
           projectdata=Project.objects.filter(name__icontains=st)
           
            
    data={
        'projectData':projectDatafinal,
        'lastpage':totalpage,
        'totalPagelist':[n+1 for n in range(totalpage)]
    }
    return render(request,"projects.html",data)

