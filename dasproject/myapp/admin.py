from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Department)
admin.site.register(AppointmentStatus)
admin.site.register(TimeSlot)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(DoctorAvailability)
admin.site.register(Appointment)
