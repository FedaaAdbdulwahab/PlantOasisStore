from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import CustomerForm

# Create your views here.
'''
def customerdet(request):
    submitted = False
    if request.method == "POST":
        form = CustomerForm(request.POST)
        form.save()
        return HttpResponseRedirect('/customer?submitted=True')
    else:
        form = CustomerForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'customer.html',{'form':form, 'submitted':submitted})
        
        '''