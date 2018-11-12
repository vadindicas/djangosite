from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    year = models.IntegerField()
    form_training = models.CharField(max_length=200)
    group = models.IntegerField()

class Specialty(models.Model):
    specialty_id = models.AutoField(primary_key=True)
    specialty_name = models.TextField(max_length=100)

class Disciplines(models.Model):
    disciplines_id = models.AutoField(primary_key=True)
    specialty = models.ForeignKey('Specialty',  on_delete=models.CASCADE)
    disciplines_name = models.TextField(max_length=100)
    hours = models.IntegerField()
    form = models.TextField(max_length=100)

class Journal(models.Model):
    j_year = models.IntegerField()
    student = models.ForeignKey('Student',  on_delete=models.CASCADE)
    disciplines = models.ForeignKey('Disciplines', on_delete=models.CASCADE)
    rate = models.IntegerField()