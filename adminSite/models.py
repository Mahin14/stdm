
from django.db import models

from student.models import StudentClass
 

class teachers(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    birthDate=models.DateField()
    address=models.TextField()
    phoneNumber=models.IntegerField()
    positon=models.CharField(max_length=200)
    className=models.ManyToManyField(StudentClass)
    teacherimage=models.ImageField(upload_to='teacher_pic')

    def __str__(self) :
        return self.first_name +" " +self.last_name

class school_notice(models.Model):
    notice_subject=models.CharField(max_length=200)
    motice_details=models.TextField()
    publish_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.notice_subject


