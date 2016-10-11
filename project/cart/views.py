# coding: utf8
from django.db import IntegrityError
from django.shortcuts import render, redirect

from models import Cart, CartItem
from xlsparse.models import Book


# Create your views here.
def cart(request):
    return render(request, 'cart/cart_all.html')


def add_cart(request, prod_id):
    cart = request.user.cart
    product = Book.objects.get(id=prod_id)
    if request.GET:
        count = request.GET['number']
        create = CartItem.objects.create(product=product, count=count)
        request.user.cart.cart.add(int(create.id))
        return redirect('cart:cart_all')
    

def remove(request, item_id):
    request.user.cart.cart.filter(id=item_id).delete()
    return redirect('cart:cart_all')



def cart_page(request, product_id):
    product = product_id
    item = Book.objects.get(id=product_id)
    try:
        create = Cart.objects.create(user=request.user)
    except IntegrityError:
        print "Cart is exist"
    return render(request, 'cart/cart.html', {'product_id': product, 'item':item })



