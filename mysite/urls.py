from django.contrib import admin
from django.urls import path
from mysite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage,name='home'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('projects/', views.projects,name='projects'),
    path('contact/', views.contact,name='contact'),
    path('login/', views.login,name='login'),
    path('information_form/', views.information_form,name='information_form'),
    path('form/', views.form,name='form'),
    path('newsdetails/<slug>', views.newsDetails,name='details'),
    path('saveenquiry/', views.saveEnquiry,name='saveenquiry'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
