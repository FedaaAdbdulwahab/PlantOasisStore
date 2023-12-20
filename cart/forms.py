from django import forms
from django.forms import ModelForm
from store.models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields  = ('first_name','last_name', 'phone' ,'email')
        labels = {
			'first_name': '',
			'last_name': '',
            'phone':'',
			'email': '',

            
		}
        
        widgets = {
                    'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
                    'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
                    'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
                    'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
                    
                    
                }