from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *

# def user_login(request):
#     if request.method == "POST":
#         uname = request.POST.get("name")
#         pwd = request.POST.get("password")
#         print(uname, pwd, 'up......................................')
#         user = authenticate(username=uname, password=pwd)
#
#         if user is not None:
#             login(request, user)
#             if user.is_superuser:
#                 return redirect('product_list')
#             else:
#                 return redirect('home')
#         else:
#             return render(request, 'registration/login.html', {"message": "invalid username or password"})
#     return render(request, 'registration/login.html')


@login_required()
def product_add(request):
    template_name = 'products/product_add.html'
    form = ProductAddForm()
    context = {'form': form}
    if request.method == "POST":
        form = ProductAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Details Successfully Added.', 'alert-success')
            return redirect('product_list')
        else:
            context = {'form': form}
            messages.success(request, 'Data is not valid.', 'alert-danger')
            return render(request, template_name, context)
    return render(request, template_name, context)


@login_required()
def product_list(request):
    if not request.user.is_superuser:
        return redirect('home')
    template_name = 'products/product_list.html'
    product_list = Products.objects.all()
    context = {'product_list':product_list}
    return render(request, template_name, context)


@login_required()
def product_details(request, pk):
    template_name = 'products/product_details.html'
    products = Products.objects.get(product_id=pk)
    context = {'product':products}
    return render(request, template_name, context)


@login_required()
def product_delete(request, pk):
    Products.objects.get(product_id=pk).delete()
    messages.success(request, 'Product details are deleted..', 'alert-success')
    return redirect('product_list')


@login_required()
def product_edit(request, pk):
    template_name = 'products/product_edit.html'
    product = Products.objects.get(product_id=pk)
    form = ProductAddForm(instance=product)
    context = {'form': form, 'product': product}
    if request.method == "POST":
        form = ProductAddForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Details Successfully Updated.', 'alert-success')
            return redirect('product_list')
        else:
            context = {'form': form}
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            return render(request, template_name, context)
    return render(request, template_name, context)



