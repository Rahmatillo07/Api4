from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=25)
    price = models.PositiveIntegerField()
    duration = models.DateField()

    def __str__(self):
        return self.name


class Teacher(models.Model):

    TEACHER_STATUS_CHOICES = (
        ('active','active'),
        ('awaiting','awaiting'),
        ('busy','busy')
    )
    EXPERIENCE_CHOICES = (
        ('senior','senior'),
        ('middle','middle'),
        ('junior','junior')
    )

    full_name = models.CharField(max_length=50)
    status = models.CharField(max_length=10,choices=TEACHER_STATUS_CHOICES,default='active')
    experience = models.CharField(max_length=10,choices=EXPERIENCE_CHOICES,default='middle')
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name



class Student(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    pr_phone = models.CharField(max_length=13)
    telegram = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    course = models.OneToOneField(Course,on_delete=models.CASCADE)
    teacher = models.OneToOneField(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
