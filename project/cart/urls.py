from django.conf.urls import url, include
from cart import views

urlpatterns = [
    url(r'^add_prod/(?P<prod_id>[0-9]+)$',views.add_cart, name='add_cart'),
    url(r'^remove/(?P<item_id>[0-9]+)$',views.remove, name='remove'),
    url(r'^cart/(?P<product_id>[0-9]+)$',  views.cart_page, name='cart_page'),
    url(r'^cart_all/$', views.cart, name='cart_all'),

    # url(r'^add/(?P<product_id>[0-9]+)$', views.add, name='add'),
]