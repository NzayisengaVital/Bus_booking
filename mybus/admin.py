from django.contrib import admin
from .models import Location
from .models import Booking
from .models import Province, District, Sector, Cell,Village

# Register your models here.
admin.site.register(Location)
admin.site.register(Booking)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Sector)
admin.site.register(Cell)
admin.site.register(Village)