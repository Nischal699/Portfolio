from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UsersForm
from service.models import Service
from news.models import News
from contactenquiry.models import contactEnquiry
from django.core.paginator import Paginator


#def aboutUS(request):
#   return HttpResponse("WELCOME TO MY PAGE")

def homePage(request):
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
    
    paginator=Paginator(servicesData,2)
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
    return render(request,"contact.html")

def portfolio(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"portfolio.html",data)

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


