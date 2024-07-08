from django.db import models



class Classroom(models.Model):
    name=models.CharField(max_length=20)
    section=models.CharField(max_length=5)


class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=50)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="classroom_students", 
                                  null=True, blank=True)
    
class StudentProfile(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE)   
    profile_picture=models.FileField(null=True,blank=True)
    phone=models.CharField(max_length=14)
    roll=models.PositiveIntegerField()
    bio=models.TextField(max_length=1000) 