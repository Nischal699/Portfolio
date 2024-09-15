from django.http import HttpResponse
from django.shortcuts import render

#def aboutUS(request):
#   return HttpResponse("WELCOME TO MY PAGE")

def homePage(request):
    data={
        'title':'Home-Page',
        'name':'Nischal'
    }
    return render(request,"index.html",data)

def about(request):
    data={
        'title':'Eduaction',
        'name':'Nischal'
    }
    return render(request,"about.html",data)

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
          n1=request.POST.get('full_name')
          name=n1
          data={
              'n1':n1,
              'full_name':name
          }
    except:
        pass
    
    return render(request,"information_form.html",data)

