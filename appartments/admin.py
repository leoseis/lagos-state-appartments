# admin.py
from django.contrib import admin
from .models import Appartment, ApartmentImage

class ApartmentImageInline(admin.TabularInline):
    model = ApartmentImage
    extra = 1

@admin.register(Appartment)
class AppartmentAdmin(admin.ModelAdmin):
    inlines = [ApartmentImageInline]
    list_display = ['title', 'price', 'address']
