from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import CartItemForm, CheckoutForm
from .models import Banner, CartItem, Category, Order, OrderItem, Page, Product

def n1(request):
    products = Product.objects.all()
    banners = Banner.objects.all()
    categories = Category.objects.all()
    pages = Page.objects.order_by('order')

    context = {
        'products': products,
        'banners': banners,
        'categories': categories,
        'pages': pages,
    }
    return render(request, 'index.html', context)

def n2(request):
    products = Product.objects.all()
    banners = Banner.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'banners': banners,
        'categories': categories,
    }
    return render(request, 'shop.html', context)

def no(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data added successfully')
        else:
            return HttpResponse(form.errors)
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form})

class n5(View):
    template_name = 'checkout.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to login if the user is not authenticated

        # Fetch the user's cart items and calculate the total amount
        cart_items = CartItem.objects.filter(user=request.user)
        total_amount = sum(item.total_price() for item in cart_items)

        context = {'cart_items': cart_items, 'total_amount': total_amount, 'form': CheckoutForm()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Fetch the user's cart items and calculate the total amount
            cart_items = CartItem.objects.filter(user=request.user)

            # Create an order
            order = Order.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                country=form.cleaned_data['country'],
                address_street=form.cleaned_data['address_street'],
                address_optional=form.cleaned_data['address_optional'],
                town_city=form.cleaned_data['town_city'],
                country_state=form.cleaned_data['country_state'],
                postcode_zip=form.cleaned_data['postcode_zip'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                create_account=form.cleaned_data['create_account'],
                account_password=form.cleaned_data['account_password'],
                note=form.cleaned_data['note'],
                
            )

            # Create order items
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    subtotal=cart_item.total_price()
                )

            # Clear the user's cart
            cart_items.delete()

            return redirect('order-confirmation')

        # If the form is not valid, log the errors and re-render the checkout page with errors
        print(form.errors)
        return render(request, self.template_name, {'form': form})

def n7(request):
    cart_items = CartItem.objects.all()
    total = sum(item.total_price() for item in cart_items)
    form = CartItemForm()

    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            cart_item = form.save(commit=False)
            cart_item.save()
            return redirect('shop-cart')

    context = {'cart_items': cart_items, 'total': total, 'form': form}
    return render(request, 'shop-cart.html', context)

def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('shop-cart')

def shop_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        product_image = request.POST.get('product_image')

        # Add the product to the cart (you need to implement this logic)
        CartItem.objects.create(
            user=request.user,  # Assuming you have a user associated with the cart
            product_id=product_id,
            product_name=product_name,
            product_price=product_price,
            product_image=product_image,
        )

    # Retrieve the cart items and render the cart template
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'your_cart_template.html', {'cart_items': cart_items})

class YourCartView(View):
    template_name = 'shop-cart.html'

    def get(self, request, *args, **kwargs):
        cart_items = CartItem.objects.all()
        total = sum(item.total_price() for item in cart_items)
        form = CartItemForm()

        context = {'cart_items': cart_items, 'total': total, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CartItemForm(request.POST)
        if form.is_valid():
            cart_item = form.save(commit=False)
            cart_item.save()
            return redirect('shop-cart')

        cart_items = CartItem.objects.all()
        total = sum(item.total_price() for item in cart_items)

        context = {'cart_items': cart_items, 'total': total, 'form': form}
        return render(request, self.template_name, context)

def n3(request):
    return render(request, 'product-details.html')


def n6(request):
    return render(request, 'contact.html')
