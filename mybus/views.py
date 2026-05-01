
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Location
from .models import Booking
from .models import Province, District, Sector, Cell, Village
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'mybus/home.html')

def search_bus(request):
    if request.method == "POST":
        from_loc = request.POST.get('from_location')
        to_loc = request.POST.get('to_location')

        buses = Location.objects.filter(
            from_location__icontains=from_loc,
            to_location__icontains=to_loc
        )

        if not buses:
            messages.warning(request, "No bus found!")
            

        return render(request, 'mybus/getBus.html', {'buses': buses})

    return render(request, 'mybus/bus.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  
        else:
            messages.error(request, "Amazina cg ijambo banga sibyo😔")

    return render(request, "mybus/login.html")

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, '***Ijambo banga mwatanze siryo!***')
            return redirect('register')
        if User.objects.filter(username = username).exists():
            messages.error(request, 'Konte yawe isanzwe ihari!')
            return redirect('register')
        #creating user
        
        user = User.objects.create_user(
            username = username,
            password = password
        )
        messages.success(request, f'Konte yawe yakozwe neza, {username}! ✔️')
        return redirect('login')
    return render(request, 'mybus/register.html')
def getbus(request):
    your_bus = Location.objects.all()
    return render(request, 'mybus/getBus.html', {'buses':your_bus})

def logout_view(request):
    logout(request)
    messages.success(request, 'Wasohotse muri system!👋')
    return redirect('home')

from .models import Booking

def book_bus(request, bus_id):
    bus = Location.objects.get(id=bus_id)

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')

        payment_method = request.POST.get('payment_method')
        travel_date = request.POST.get('date')

        booking = Booking.objects.create(
                user=request.user,
                bus=bus,
                date=travel_date,
        )

        messages.success(request, f"Bus yanyu yabitswe neza! 🎉👏👏 ***Bika indi👆")
        messages.error(request, f"Token yawe ni: {booking.token}")
        return redirect('home')

    return render(request, 'mybus/book.html', {'bus': bus})
def contact(request):
    return render(request, 'mybus/contact.html')

def about(request):
    return render(request, 'mybus/about.html')

def designer(request):
    return render(request, 'mybus/designer.html')
def services(request):
    provinces = Province.objects.all()
    return render(request, 'mybus/services.html', {'provinces': provinces})

def load_districts(request):
    province_id = request.GET.get('province_id')
    districts = District.objects.filter(province_id=province_id)

    data = list(districts.values('id', 'name'))
    return JsonResponse(data, safe=False)
    
def load_sectors(request):
    district_id = request.GET.get('district_id')
    sectors = Sector.objects.filter(district_id=district_id)

    data = list(sectors.values('id', 'name'))
    return JsonResponse(data, safe=False)

def load_cells(request):
    # Get selected sector id from frontend (AJAX)
    sector_id = request.GET.get('sector_id')

    # Filter cells based on selected sector
    cells = Cell.objects.filter(sector_id=sector_id)

    # Convert queryset to JSON format (id + name only)
    data = list(cells.values('id', 'name'))

    # Return JSON response
    return JsonResponse(data, safe=False)

def load_villages(request):
    cell_id = request.GET.get('cell_id')

    villages = Village.objects.filter(cell_id=cell_id)

    data = list(villages.values('id', 'name'))

    return JsonResponse(data, safe=False)