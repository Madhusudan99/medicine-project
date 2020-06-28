from django.contrib import admin
from .models import Doctor, Patient, Drug, Prescription,Prescription_direction_frequency_count, Prescription_direction_day_week_month

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Drug)
admin.site.register(Prescription)
admin.site.register(Prescription_direction_frequency_count)
admin.site.register(Prescription_direction_day_week_month)