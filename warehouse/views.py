from django.shortcuts import render
from .models import Product
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from django.core.paginator import Paginator

def product_list(request):
    products = Product.objects.all().order_by('published_date')
    return render(request, 'warehouse/product_list.html', {'products': products})


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)  # MongoEngine Query
    except Product.DoesNotExist:
        raise Http404("Product not found")
    return render(request, 'warehouse/product_detail.html', {'product': product})

def product_new(request):
    if request.method =="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = Product(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                category = form.cleaned_data['category'],
                price = form.cleaned_data['price'],
                brand = form.cleaned_data['brand'],
                quantity = form.cleaned_data['quantity'],
            )
            product.author = request.user
            product.published_date = timezone.now()
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'warehouse/product_edit.html', {'form': form})

def product_edit(request, pk):
    try:
        product = Product.objects.get(pk=pk)  # MongoEngine Query
    except Product.DoesNotExist:
        raise Http404("Product not found")
    if request.method =="POST":
        form = ProductForm(request.POST, initial=product.to_mongo().to_dict())
        if form.is_valid():
            product.update(**form.cleaned_data)
            product.author = request.user
            product.published_date = timezone.now()
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(initial=product.to_mongo().to_dict())
    return render(request, 'warehouse/product_edit.html', {'form': form})

def product_delete(request, pk):
    try:
        product = Product.objects.get(pk=pk)  # MongoEngine Query
    except Product.DoesNotExist:
        raise Http404("Product not found")
    product.delete()
    return redirect('product_list')


def product_fetch(request, name):
    products = Product.objects.filter(name__icontains=name).order_by('name')
    # print("Products: ",products)
    paginator = Paginator(products, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    # print(page_obj)
    return render(request, 'warehouse/product_fetch.html', {'page_obj': page_obj})



def error_400(request, exception):
    return render(request, 'errors/400.html', status=400)

def error_401(request, exception):
    return render(request, 'errors/401.html', status=401)

def error_403(request, exception):
    return render(request, 'errors/403.html', status=403)

def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def error_500(request):
    return render(request, 'errors/500.html', status=500)

def error_502(request, exception):
    return render(request, 'errors/502.html', status=502)

def error_503(request, exception):
    return render(request, 'errors/503.html', status=503)

# Create your views here.
