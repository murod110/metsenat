from django.db import models
from datetime import datetime
from .fuctions import lines
from django.db.models.signals import post_save
from django.dispatch import receiver

# Statistics
class Statistics(models.Model):
    month = models.CharField(max_length=150)
    year = models.CharField(max_length=150)
    student_count = models.IntegerField(null=True, default=0)
    sponsor_count = models.IntegerField(null=True, default=0)

    def __str__(self) -> str:
        return super().__str__()


# Sponsor Model
persons = (
    ('jismoniy shaxs', 'jismoniy shaxs'),
    ('yuridik shaxs', 'yuridik shaxs')
)

prices = (
    ('1000000', 1000000),
    ('5000000', 5000000),
    ('7000000', 7000000),
    ('10000000', 10000000),
    ('30000000', 30000000),
    ('boshqa', 'boshqa')
)



CHOICE = (
    ('yangi', 'yangi'),
    ('moderatsiyada', 'moderatsiyada'),
    ('tasdiqlangan', 'tasdiqlangan'),
    ('bekor qilingan', 'bekor qilingan')
)

class Sponsor(models.Model):
    full_name = models.CharField(max_length=150)
    person_type = models.CharField(choices=persons, max_length=150)
    phone = models.CharField(max_length=150)
    prices = models.CharField(max_length=100, choices=prices)
    organization = models.CharField(max_length=150, null=True, blank=True)
    spent = models.IntegerField(null=True, default=0)
    other_price = models.CharField(max_length=100,blank=True, null=True)
    dt = models.DateField(default=datetime.today())
    status = models.CharField(max_length=100, choices=CHOICE, default="yangi", null=True, blank=True)

    def __str__(self):
        return self.full_name
    
    @property 
    def intprice(self):
        return int(prices)
    
    @property
    def residual(self):
        if self.prices == "boshqa":
            return int(self.other_price)-self.spent
        else:
            return int(self.prices)-self.spent
    
# Student Model

student_type = (
    ('bakalavr', 'bakalavr'),
    ('magistr', 'magistr'),
    ('boshqa', 'boshqa')
)
class Student(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    otm = models.CharField(choices=lines(), max_length=500)
    type = models.CharField(max_length=150, choices=student_type)
    contract = models.CharField(max_length=150)
    appected = models.IntegerField(default=0)
    dt = models.DateField(default=datetime.today())
    

    def __str__(self) -> str:
        return self.full_name
    
    @property
    def max_needed(self):
        return int(self.contract)-self.appected

class Sponsor_Attachment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor,on_delete=models.CASCADE)
    sponsorship = models.IntegerField()

    def __str__(self) -> str:
        return super().__str__()



@receiver(post_save, sender=Student)
def update_student_count(sender, instance, created, **kwargs):
    if created:
        year = instance.dt.year 
        month = instance.dt.month

        stats, created = Statistics.objects.get_or_create(year=year, month=month)
        stats.student_count += 1
        stats.save()

@receiver(post_save, sender=Sponsor)
def update_sponsor_count(sender, instance, created, **kwargs):
    if created:
        year = instance.dt.year 
        month = instance.dt.month

        stats, created = Statistics.objects.get_or_create(year=year, month=month)
        stats.sponsor_count += 1
        stats.save()

@receiver(post_save, sender=Sponsor_Attachment)
def update_spent_and_appected(sender, instance, created, **kwargs):
    if created:
        student = instance.student.id
        sponsor = instance.sponsor.id
        sponsorship = instance.sponsorship
        student = Student.objects.get(pk = student)
        sponsor = Sponsor.objects.get(pk = sponsor)
        student.appected += sponsorship
        sponsor.spent += sponsorship
        student.save()
        sponsor.save()