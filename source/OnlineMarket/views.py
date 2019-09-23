from django.shortcuts import render, get_object_or_404, redirect

from OnlineMarket.forms import StoreForm
from OnlineMarket.models import Product, PRODUCT_CATEGORY_CHOICES


def index_view(request):
    products = Product.objects.exclude(amount=0).order_by('category', 'name')
    return render(request, 'index.html', context={
        'products': products,
    })


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product_detail.html', context={
        'product': product,
    })


def product_create_view(request):
    if request.method == 'GET':
        form = StoreForm()
        return render(request, 'product_create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = StoreForm(data=request.POST)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                amount=form.cleaned_data['amount'],
                price=form.cleaned_data['price']
            )
            response = redirect('index')
            return response
        else:
            return render(request, 'product_create.html', context={
                'form': form
            })


def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = StoreForm(data={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'amount': product.amount,
            'price': product.price
        })
        return render(request, 'product_update.html', context={
            'category': PRODUCT_CATEGORY_CHOICES,
            'product': product,
            'form': form
        })
    elif request.method == 'POST':
        form = StoreForm(data=request.POST)

        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.amount = form.cleaned_data['amount']
            product.price = form.cleaned_data['price']
            product.save()
        else:
            return render(request, 'product_update.html', context={'form': form, 'product': product})
    return redirect('index')


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'product_delete.html', context={
            'product': product
        })
    elif request.method == 'POST':
        product.delete()
        return redirect('index')