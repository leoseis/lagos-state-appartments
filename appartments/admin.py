from django.contrib import admin
from .models import Appartment, ApartmentImage, Agent  # Added Agent import

class ApartmentImageInline(admin.TabularInline):
    model = ApartmentImage
    extra = 1

@admin.register(Agent)  # Register Agent model
class AgentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']

@admin.register(Appartment)
class AppartmentAdmin(admin.ModelAdmin):
    inlines = [ApartmentImageInline]
    list_display = ['title', 'price', 'address', 'agent']  # Show agent in list view
    fields = ['title', 'price', 'num_bedrooms', 'num_bathrooms', 
             'square_footage', 'address', 'cover_image', 'agent']  # Explicit fields