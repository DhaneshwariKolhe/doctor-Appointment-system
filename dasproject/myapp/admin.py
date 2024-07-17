from django.contrib import admin
from .models import *


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_name',)
    search_fields = ('dept_name',)


@admin.register(AppointmentStatus)
class AppointmentStatusAdmin(admin.ModelAdmin):
    list_display = ('status',)
    search_fields = ('status',)


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('timeslot',)
    search_fields = ('timeslot',)
    list_filter = ('timeslot',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','Dept_name','email','contact_number')
    search_fields = ('first_name','last_name','contact_number')
    list_filter = ('Dept_name',)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','contact_number')
    search_fields = ('first_name','last_name','contact_number')


@admin.register(DoctorAvailability)
class DoctorAvailabilityAdmin(admin.ModelAdmin):
    list_display = ['Doctor','day_of_wk']
    search_fields =['Doctor','day_of_wk']
    list_filter = ['Doctor','day_of_wk','timeslot']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['Doctor','patient','appointment_date','timeslot','appointment_status'] 
    list_filter = ['Doctor','appointment_date','timeslot','appointment_status']
    

