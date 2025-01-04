from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UsersForm

#def aboutUS(request):
#   return HttpResponse("WELCOME TO MY PAGE")

def homePage(request):
    data={
        'title':'Home-Page',
        'name':'Nischal'
    }
    return render(request,"index.html",data)

def about(request):
    if request.method=="GET":
        output=request.GET.get('output')
    
    return render(request,"about.html",{'full_name':output})

def services(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"services.html",data)

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


