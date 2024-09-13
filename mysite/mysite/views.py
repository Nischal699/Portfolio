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

def form(request):
    name=0
    address=0
    try:
        #n1=(request.GET['num1'])
        #n2=(request.GET['num2'])
        
        n1=request.GET.get('num1')
        n2=request.GET.get('num2')
        
        name=n1
        address=n2
        
    except:
        pass
    
    return render(request,"form.html",{'naame':name,'addr':address})

