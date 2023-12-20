from django import forms
from django.forms import ModelForm
from .models import CustomerDetails

class CustomerForm(ModelForm):
    class Meta:
        model = CustomerDetails
        fields  = ('first_name','last_name', 'phone', 'address' ,'email')
        labels = {
			'first_name': '',
			'last_name': '',
            'phone':'',
            'address':'',
			'email': '',

            
		}
        
        widgets = {
                    'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
                    'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
                    'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
                    'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
                    'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
                    
                    
                }