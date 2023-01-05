from django.shortcuts import render, redirect, HttpResponse
from django.template.loader import get_template
from products.models import *
from xhtml2pdf import pisa
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator
import razorpay
from .models import Payment
from .forms import PaymentForm
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    products = Products.objects.filter(active_inactive=True)
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, 'purchase/home.html', context)


@login_required()
def cart_items(request):
    if request.method == "GET":
        template_name = 'purchase/cart_list.html'
        user = request.user
        cart_items = Cart.objects.filter(user=user, bought=False)
        total_amount = 0
        for i in cart_items:
            if i.amount !=  None:
                print(i.amount, 'am')
                total_amount += float(i.amount)

        total_amount = "{:.2f}".format(total_amount)
        customer = request.user.id
        context = {'cart_items': cart_items, 'customer': customer, 'total_amount': total_amount}
        return render(request, template_name, context)


@login_required()
def cart(request, pk ):
    if request.method == "GET":
        item = Products.objects.get(product_id=pk)
        cart_item_exist = Cart.objects.filter(user=request.user.id, product__product_id=pk).exists()
        if cart_item_exist:
            messages.success(request, f"{item.product_name} already added to cart", 'alert-danger')
            return redirect('home')

        else:
            amt =  float(item.price)
            Cart.objects.create(user=request.user, product=item, quantity=1, amount=amt)

        return redirect('cart_items')


@login_required()
def remove_from(request, pk):
    Cart.objects.filter(cart_id=pk).delete()
    customer = request.user.id
    return redirect('cart_items')


@login_required()
def cart_plus(request, pk):
    cart_old = Cart.objects.get(cart_id=pk)
    new_quantity = int(cart_old.quantity) + 1
    new_amt = float(cart_old.amount) + float(cart_old.product.price)
    new_amt = "{:.2f}".format(new_amt)
    Cart.objects.filter(cart_id=pk).update(
        quantity=new_quantity,
        amount=new_amt,
    )
    return redirect('cart_items')


@login_required()
def cart_minus(request, pk):
    cart_old = Cart.objects.get(cart_id=pk)
    if cart_old.quantity == '1':
        pass
    else:
        new_quantity = int(cart_old.quantity) - 1
        new_amt = float(cart_old.amount) - float(cart_old.product.price)
        new_amt = "{:.2f}".format(new_amt)
        Cart.objects.filter(cart_id=pk).update(
            quantity=new_quantity,
            amount=new_amt,
        )
    return redirect('cart_items')




@login_required()
def payment_add(request, pk):
    cart = Cart.objects.get(cart_id=pk)
    if request.method == "POST":

        name = request.POST.get('name')
        amount = float(request.POST.get('amount')) * 100
        client = razorpay.Client(auth=('rzp_test_eSFDI8B2mj7DFR', 'LwHsHl6s5e0zvUV26ZaopAea'))
        response_payment = client.order.create(dict(amount=amount,
                                                    currency='INR')
                                               )
        order_id = response_payment['id']
        order_status = response_payment['status']

        if order_status == 'created':
            cold_coffee = Payment(
                name=name,
                amount=amount,
                order_id=order_id,
                cart = cart
            )
            cold_coffee.save()
            response_payment['name'] = name

            form = PaymentForm(request.POST or None)
            return render(request, 'purchase/payment_add.html', {'form': form, 'payment': response_payment, "pk":pk})
    name = str(request.user)
    form = PaymentForm(initial={'name':name,'amount':cart.amount})
    return render(request, 'purchase/payment_add.html', {'form': form, 'pk':pk})


@login_required()
def payment_status(request, pk):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }


    client = razorpay.Client(auth=('rzp_test_eSFDI8B2mj7DFR', 'LwHsHl6s5e0zvUV26ZaopAea'))

    try:
        status = client.utility.verify_payment_signature(params_dict)
        order_item = Payment.objects.get(order_id=response['razorpay_order_id'])
        order_item.razorpay_payment_id = response['razorpay_payment_id']
        order_item.paid = True
        order_item.save()
        order_item.cart.bought = True
        order_item.cart.save()

        return render(request, 'purchase/payment_status.html', {'status': True, "pk":pk})
    except:
        return render(request, 'purchase/payment_status.html', {'status': False, "pk":pk})

@login_required()
def download_invoice(request, pk):
    template_path = 'purchase/invoice_pdf.html'
    cart = Cart.objects.get(cart_id=pk)
    context = {'cart':cart}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="bill.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response