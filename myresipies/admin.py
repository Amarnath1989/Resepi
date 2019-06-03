from django.contrib import admin
from.models import Resepi

# Register your models here.
class Resepi_Admin(admin.ModelAdmin):
    list_display = ['name','ingredients','process','image']
admin.site.register(Resepi,Resepi_Admin)
