from django import forms

class UsersForm(forms.Form):
    login=forms.CharField(label="Username",
                          required=False,
                          widget=forms.TextInput(attrs={'class':"form-control"
                                                        }))
    password=forms.CharField(label="Password",
                             required=False,
                             widget=forms.TextInput(attrs={'class':"form-control"
                                                           }))