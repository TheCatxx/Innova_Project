from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')
    category_list = Categoria.objects.all()
    context = {'product_list': product_list, 'category_list':category_list}
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    category_list = Categoria.objects.all()
    context = {'producto': producto, 'category_list':category_list}
    return render(request, 'producto.html', context)



def categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    categoria_list = Categoria.objects.all()
    product_list=Producto.objects.order_by('nombre')
    context = {'categoria': categoria, 'product_list':product_list, 'categoria_list': categoria_list}
    return render(request, 'categoria.html', context)
