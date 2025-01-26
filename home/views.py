from django.shortcuts import render, HttpResponse
from .models import Storeinstruments, Cart, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


# views.py
from django.shortcuts import render,get_object_or_404, redirect
from .models import Storeinstruments

def home(request):
    images = Storeinstruments.objects.all().order_by('-created_at')
    context = {
        'images': images
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')


# views.py
def instruments(request):
    instruments = Storeinstruments.objects.all().order_by('-created_at')
    context = {
        'instruments': instruments
    }
    return render(request, 'instruments.html', context)


def contact(request):
    return render(request, 'contact.html')

# Create your views here.
@login_required
def view_cart(request):
    # Fetch cart items for the logged-in user
    cart_items = Cart.objects.filter(user=request.user)
    
    # Calculate the total number of items in the cart
    cart_item_count = sum(item.quantity for item in cart_items)
    
    # Calculate the total price
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    # Pass cart items, total price, and cart item count to the template
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'cart_item_count': cart_item_count,
    })

# Cart views
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Storeinstruments, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f"{Storeinstruments.name} added to your cart.")
    return redirect(request.META.get('HTTP_REFERER', 'products'))  # Redirect back to the same page

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
    
    if cart_item.quantity > 1:
        # Decrement the quantity by 1
        cart_item.quantity -= 1
        cart_item.save()
        messages.success(request, f"One {cart_item.product.name} removed from your cart.")
    else:
        # Delete the item if the quantity is 1
        cart_item.delete()
        messages.success(request, f"{cart_item.product.name} removed from your cart.")
    
    return redirect(request.META.get('HTTP_REFERER', 'view_cart'))  # Redirect back to the same page



def search(request):
    query = request.GET.get('q')
    products = Storeinstruments.objects.all()
    
    if query:
        products = Storeinstruments.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(sport__name__icontains=query)
        )
    
    cart_item_count = get_cart_item_count(request.user)
    return render(request, 'products.html', {
        'products': products,
        'cart_item_count': cart_item_count,
        'query': query
    })



@login_required
def remove_all_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
    cart_item.delete()
    messages.success(request, f"All {cart_item.product.name} removed from your cart.")
    return redirect(request.META.get('HTTP_REFERER', 'view_cart'))

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def process_checkout(request):
    if request.method == 'POST':
        cart_items = Cart.objects.filter(user=request.user)
        
        if not cart_items:
            messages.error(request, "Your cart is empty.")
            return redirect('view_cart')
            
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        shipping_address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')
        
        # Validate credit card if needed
        if payment_method == 'Credit Card':
            card_number = request.POST.get('card_number')
            expiry_date = request.POST.get('expiry_date')
            cvv = request.POST.get('cvv')
            
            if not card_number or not expiry_date or not cvv:
                messages.error(request, "Please provide valid credit card details.")
                return redirect('checkout')
        
        # Create order
        order = Order.objects.create(
            user=request.user,
            total_price=sum(item.product.price * item.quantity for item in cart_items),
            shipping_address=shipping_address,
            payment_method=payment_method,
            email=email,
        )
        
        # Process each cart item
        for item in cart_items:
            # Check if enough stock is available
            if item.product.stock < item.quantity:
                messages.error(request, f"Not enough stock for {item.product.name}")
                order.delete()
                return redirect('view_cart')
                
            # Reduce stock
            item.product.stock -= item.quantity
            item.product.save()
            
            # Create order item
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )
        
        # Clear cart
        cart_items.delete()
        messages.success(request, "Your order has been placed successfully!")
        return redirect('index')
        
    return redirect('view_cart')


def checkout(request):
    # Fetch cart items for the logged-in user
    # cart_items = Cart.objects.filter(user=request.user)
    
    # Calculate the total price
    # total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    # Pass cart items and total price to the checkout template
    return render(request, 'checkout.html')
    # , {
    #     'cart_items': cart_items,
    #     'total_price': total_price,
    # })


def get_cart_item_count(user):
    if user.is_authenticated:
        return sum(item.quantity for item in Cart.objects.filter(user=user))
    return 0
