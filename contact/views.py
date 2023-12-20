from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm, CustomerForm

# Create your views here.

def contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        form.save()
        return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'contact.html',{'form':form, 'submitted':submitted})
    
    
def customerdet(request):
    submitted = False
    if request.method == "POST":
        form = CustomerForm(request.POST)
        form.save()
        return HttpResponseRedirect("/customer?submitted=True")
    else:
        form = CustomerForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'customer.html',{'form':form, 'submitted':submitted})