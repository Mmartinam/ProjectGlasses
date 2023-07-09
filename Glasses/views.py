from django.shortcuts import render, redirect, get_object_or_404
from Glasses.models import Glasses, Order, Client
from django.contrib.auth import authenticate, login
from .forms import GlassesForm
from django.contrib import messages
from django.db.models import Sum
from .forms import CustomerForm
# Create your views here.


def index(request):

    if request.method == 'POST':
        form = GlassesForm(request.POST, request.FILES)
        if form.is_valid():
            glass = form.save(commit=False)
            glass.user = request.user
            glass.photo = form.cleaned_data['photo']
            glass.save()
            return redirect('index')

    if 'q' in request.GET:
        q = request.GET['q']
        glasses = Glasses.objects.filter(name__contains=q)
    else:
        glasses = Glasses.objects.all()

    context = {"index": glasses, "form": GlassesForm}
    return render(request, "index.html", context=context)


def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Incorrect username or password. Please try again.")
            return redirect('log_in')
    return render(request, "log_in.html")


def details(request, glasses_id):

    glasses = get_object_or_404(Glasses, id= glasses_id)
    context = {'glasses': glasses}

    return render(request, "details.html", context)


def add_to_cart(request, glasses_id):
    glasses = Glasses.objects.get(id=glasses_id)
    order, created = Order.objects.get_or_create(glasses=glasses, defaults={'quantity': 1, 'total_price': glasses.price})
    if not created:
        order.quantity += 1
        order.total_price += glasses.price
        order.save()
    return redirect('cart')


def cart(request):
    orders = Order.objects.all()
    total_price = orders.aggregate(total_price=Sum('total_price'))['total_price'] or 0

    return render(request, 'cart.html', {'orders': orders, 'total_price': total_price})


def delete_from_cart(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('cart')


def checkout(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('thank_you')
    else:
        form = CustomerForm()

    return render(request, 'checkout.html', {'form': form})


def thank_you(request):

    return render(request, 'thank_you.html')
