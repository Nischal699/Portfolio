from django.http import HttpResponse
from django.shortcuts import render

#def aboutUS(request):
#   return HttpResponse("WELCOME TO MY PAGE")

def rough(request):
    data={
        'title':'Home-Page',
        'name':'Nischal',
        'numbers':[],
        'course':['php','java','python'],
        'student_details':[
            {'name':'nischal','address':'kamalbinayak'},
            {'name':'nehal','address':'nagarkot'}
        ]
    }
    return render(request,"rough.html",data)

def homePage(request):
    data={
        'title':'Home-Page',
        'name':'Nischal'
    }
    return render(request,"index.html",data)

def education(request):
    data={
        'title':'Eduaction',
        'name':'Nischal'
    }
    return render(request,"education.html",data)

def skills(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"skills.html",data)

def projects(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"projects.html",data)

def achievements(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"achievements.html",data)

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

