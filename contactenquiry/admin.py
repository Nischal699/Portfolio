from django.contrib import admin
from contactenquiry.models import contactEnquiry

class EnquiryAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','message')
    
admin.site.register(contactEnquiry,EnquiryAdmin)
# Register your models here.
