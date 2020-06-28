from django.db import models

# Create your models here.

class Doctor(models.Model):
	full_name = models.CharField(max_length=50)
	qualification = models.CharField(max_length=50)
	address = models.TextField()
	license_no = models.CharField(max_length=20)

	def __str__(self):
		return self.full_name


class Patient(models.Model):
	full_name = models.CharField(max_length=50)
	dob = models.DateField()
	age = models.IntegerField()
	address = models.TextField()
	patient_visiting_date = models.DateField(auto_now=True)
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

	def __str__(self):
		return self.full_name


class Drug(models.Model):
	drug_name = models.CharField(max_length=100)

	def __str__(self):
		return self.drug_name


class Prescription_direction_frequency_count(models.Model):
	frequency_count = models.CharField(max_length=100) # How many times medicine should be taken in a day/week/month

	def __str__(self):
		return self.frequency_count


class Prescription_direction_day_week_month(models.Model):
	day_week_month = models.CharField(max_length=50)   # How many in a day/week/month

	def __str__(self):
		return self.day_week_month


class Prescription(models.Model):
	prescription_id = models.IntegerField()
	prescription_date = models.DateField()
	drug_name = models.ForeignKey(Drug, on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	prescription_direction_frequency_count = models.ForeignKey(Prescription_direction_frequency_count, on_delete=models.CASCADE)
	prescription_direction_day_week_month = models.ForeignKey(Prescription_direction_day_week_month, on_delete=models.CASCADE)

	def __str__(self):
		return self.patient.full_name

		