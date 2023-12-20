from django.shortcuts import redirect, render

from cart.cart import Cart


'''
def index( request ):
    
    cartitems = Cart.objects.filter(customer=request.customer)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.price * item.quantity
    
    context = {'cartitems':cartitems, 'total_price':total_price}
    return render(request, 'checkout.html', context)


'''