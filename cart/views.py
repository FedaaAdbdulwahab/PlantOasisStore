from urllib import request
from django.shortcuts import redirect, render, get_object_or_404

from cart.forms import CustomerForm
from .cart import Cart
from store.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

def cart_summary(request):
	# Get the cart
	cart = Cart(request)
	cart_products = cart.get_prods
	quantities = cart.get_quants
	return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities})




def cart_add(request):
	# Get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		# lookup product in DB
		product = get_object_or_404(Product, id=product_id)
		
		# Save to session
		cart.add(product=product, quantity=product_qty)

		# Get Cart Quantity
		cart_quantity = cart.__len__()

		# Return resonse
		# response = JsonResponse({'Product Name: ': product.name})
		response = JsonResponse({'qty': cart_quantity})
		return response

def cart_delete(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		# Call delete Function in Cart
		cart.delete(product=product_id)

		response = JsonResponse({'product':product_id})
		#return redirect('cart_summary')
		return response


def cart_update(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		cart.update(product=product_id, quantity=product_qty)

		response = JsonResponse({'qty':product_qty})
		#return redirect('cart_summary')
		return response


def checkout(request):
	cart = Cart(request)
	cart_products = cart.get_prods
	quantities = cart.get_quants
	return render(request, "checkout.html", {"cart_products":cart_products, "quantities":quantities})

'''
def order(request):
    if request.method=="POST":
        orderForm=OrderForm()
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        orderForm.fname=fname
        orderForm.lname=lname
        orderForm.email=email
        orderForm.save()
        return HttpResponse("<h1>Thanks For Contacting Us!</h1>")    
    return render(request, 'order.html')
'''    
	    

'''
def index(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('fname')
        email=request.POST.get('email')
        contact.name=name
        contact.email=email
        contact.save()
        return HttpResponse("<h1>Thanks For Contacting Us!</h1>")
        
    return render(request, 'index.html')

'''
def order(request):
	return render(request, "order.html")


# Create your views here.

def customer(request):
    submitted = False
    if request.method == "POST":
        form = CustomerForm(request.POST)
        form.save()
        return HttpResponseRedirect('/checkout?submitted=True')
    else:
        form = CustomerForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'checkout.html',{'form':form, 'submitted':submitted})


def customerdet(request):
	return render(request, 'customerdet.html')