from django.contrib import admin
from .models import ServiceCategory, Service, Master, Appointment


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'duration', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'experience', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('full_name', 'position')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'car', 'service', 'date', 'status', 'created_at')
    list_filter = ('status', 'date', 'service')
    search_fields = ('name', 'phone', 'car')
    date_hierarchy = 'date'