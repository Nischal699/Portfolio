from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UsersForm
from service.models import Service
from news.models import News

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

def newsDetails(request,newsid):
    newsDetails=News.objects.get(id=newsid )
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
    data={
        'servicesData':servicesData,
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"services.html",data)

def portfolio(requests):
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


