from django import forms
from django.forms import ModelForm
from .models import Contact, CustomerDetails

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields  = ('first_name','last_name', 'email', 'message')
        labels = {
			'first_name': '',
			'last_name': '',
			'email': '',
			'message': '',	
		}
        
        widgets = {
                    'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
                    'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
                    'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
                    'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message'}),
                    
                }
        
        

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