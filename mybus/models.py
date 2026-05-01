from django.db import models
import uuid




# Create your models here.
class Location(models.Model):
    busname = models.CharField(max_length=100)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    price = models.IntegerField()
    time = models.TimeField()

    def __str__(self):
        return f" {self.busname} From: {self.from_location} To: {self.to_location} Price: {self.price} Time: {self.time}"


from django.contrib.auth.models import User

def generate_token():
    return "BUS-" + str(uuid.uuid4())[:8].upper()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=20, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = generate_token()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} booked {self.bus.busname}"
    

  

class Province(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='districts')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='sectors')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
   
    def __str__(self):
        return self.name




class Cell(models.Model):
    # Keep your existing integer ID (default primary key)
   
    name = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='cells')

    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name

 
    

   


class Village(models.Model):
    name = models.CharField(max_length=100)
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE, related_name='villages')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name