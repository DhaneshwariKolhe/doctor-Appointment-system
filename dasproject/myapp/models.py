from django.db import models

# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.dept_name


class AppointmentStatus(models.Model):
    status = models.CharField(max_length=50)
    # active, canceled, expired, complete
    def __str__(self) -> str:
        return self.status
    

class TimeSlot(models.Model):
    timeslot = models.CharField(max_length=50)
    #11am-12noon, 1pm-2pm etc

    def __str__(self) -> str:
        return self.timeslot
    

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Dept_name = models.ForeignKey(Department,on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    contact_number = models.BigIntegerField()

    def __str__(self) -> str:
        return f"Dr. {self.first_name} {self.last_name}"
    

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contact_number = models.BigIntegerField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    


class DoctorAvailability(models.Model):
    day_of_week = (
    ("Mon", "Monday"),
    ("Tue", "TuesDay"),
    ("Wed", "Wednesday"),
    ("Thr", "Thrusday"),
    ("Fri", "Friday"),
    ("Sat", "Saturday"),
    ("Sun", "Sunday")
    )
# 
    Doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    day_of_wk = models.CharField('Type',max_length=10,choices=day_of_week,default='Monday')
    timeslot = models.ManyToManyField(TimeSlot)

    # def __str__(self) -> str:
    #     return self.Doctor
    
class Appointment(models.Model):
    Doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    appointment_date = models.DateField(null=False)
    timeslot = models.ForeignKey(TimeSlot,on_delete=models.CASCADE)
    appointment_status = models.ForeignKey(AppointmentStatus,on_delete=models.CASCADE)
    
# validation required with doctor timeslot day of wk and status will be updated automatically
# contact number validation also required