from django.shortcuts import render
from .models import Product, Category
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, CategoryForm
from django.core.paginator import Paginator
from .product_service import ProductService
from .category_service import CategoryService
from django.http import Http404
def product_list(request):
    products = ProductService.list_all_products()
    # products = Product.objects.all().order_by('published_date')
    return render(request, 'warehouse/product_list.html', {'products': products})


def product_detail(request, pk):
    try:
        product = ProductService.get_product_by_id(pk)
        # product = Product.objects.get(pk=pk)  # MongoEngine Query
    except Product.DoesNotExist:
        raise Http404("Product not found")
    return render(request, 'warehouse/product_detail.html', {'product': product})

def product_new(request):
    if request.method =="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product_data = {
                'name': form.cleaned_data['name'],
                'description': form.cleaned_data['description'],
                'category': form.cleaned_data['category'],
                'price': form.cleaned_data['price'],
                'brand': form.cleaned_data['brand'],
                'quantity': form.cleaned_data['quantity'],
                # 'author': request.user,
                'published_date': timezone.now(),
            }
            # product.author = request.user
            # product.published_date = timezone.now()
            # product.save()
            product = ProductService.add_product(product_data, request)
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'warehouse/product_edit.html', {'form': form})

def product_edit(request, pk):
    try:
        product = ProductService.get_product_by_id(pk)  # MongoEngine Query
    except Product.DoesNotExist:
        raise Http404("Product not found")
    if request.method =="POST":
        form = ProductForm(request.POST, initial=product.to_mongo().to_dict())
        if form.is_valid():
            updated_data ={**form.cleaned_data}
            product = ProductService.modify_product(pk, updated_data)
            # product.update(**form.cleaned_data)
            # product.author = request.user
            # product.published_date = timezone.now()
            # product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(initial=product.to_mongo().to_dict())
    return render(request, 'warehouse/product_edit.html', {'form': form})

def product_delete(request, pk):
    # try:
    success=ProductService.remove_product(pk)
    if not success:
        raise Http404("Product not found")
        # product = ProductService.get_product_by_id(pk)  # MongoEngine Query
    # except Product.DoesNotExist:
    #     raise Http404("Product not found")
    # product.delete()
    return redirect('product_list')


def product_fetch(request, name):
    products = ProductService.fetch_product(name)
    # products = Product.objects.filter(name__icontains=name).order_by('name')
    # print("Products: ",products)
    paginator = Paginator(products, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    # print(page_obj)
    return render(request, 'warehouse/product_fetch.html', {'page_obj': page_obj})

def product_category(request):
    categories = CategoryService.list_all_categories()
    # products = Product.objects.all().order_by('published_date')
    return render(request, 'warehouse/product_category.html', {'categories': categories})


def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category_data = {
                'title': form.cleaned_data['title'],
                'description': form.cleaned_data['description'],
                'published_date': timezone.now()
            }

            CategoryService.add_category(category_data, request)
            return redirect('product_category')
        
    else:
        form = CategoryForm()
    return render(request, 'warehouse/category_edit.html', {'form': form})


def category_detail(request, pk):
    category=CategoryService.get_category_by_id(pk)
    categoryproducts = CategoryService.fetch_categoryproducts(pk)
    paginator = Paginator(categoryproducts, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    if not category:
        raise Http404("Category Not Found")
    return render(request, 'warehouse/category_detail.html', {'category': category,
                                                              'page_obj':page_obj})


def category_edit(request, pk):
    category = CategoryService.get_category_by_id(pk)
    if not category:
        raise Http404("Category Not Found")
    if request.method == "POST":
        form = CategoryForm(request.POST, initial=category.to_mongo().to_dict())
        if form.is_valid():
            updated_data={**form.cleaned_data}
            category=CategoryService.modify_category(pk, updated_data)
            return redirect('category_detail', pk= category.pk)
    else:
        form = CategoryForm(initial=category.to_mongo().to_dict())
    return render(request, 'warehouse/category_edit.html', {'form':form})



def category_delete(request, pk):
    success=CategoryService.remove_category(pk)
    if not success:
        raise Http404("Category not found")
    return redirect('product_category')

def category_fetch(request, pk):
    categoryproducts = CategoryService.fetch_categoryproducts(pk)
    paginator = Paginator(categoryproducts, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'warehouse/categoryprod_fetch.html', {'page_obj':page_obj})

def product_new_cat(request, cat, pk):
    if request.method == "POST":
        form= ProductForm(request.POST)
        form.category= cat
        if form.is_valid(): 
            product_data={
            'name': form.cleaned_data['name'],
            'description': form.cleaned_data['description'],
            'category': cat,
            'price': form.cleaned_data['price'],
            'brand': form.cleaned_data['brand'],
            'quantity': form.cleaned_data['quantity'],
            # 'author': request.user,
            'published_date': timezone.now(),
        }
        ProductService.add_product(product_data, request)
        return redirect('category_detail', pk=pk)
    else:
        form = ProductForm()
    return render(request, 'warehouse/product_edit.html', {'form': form})    




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
