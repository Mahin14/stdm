from django.db import models
from random import randint

import datetime
x = datetime.datetime.now()
def random_num():
    reg= str(x.year)+str(randint(000000,999999))
    return reg



class StudentClass(models.Model):
    class_name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.class_name
# Create your models here.
class students(models.Model):
    registration_no=models.CharField(default=random_num(),max_length=100,unique=True,primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    roll=models.IntegerField( blank=True,null=True)
    birthDate=models.DateField()
    details_address=models.TextField( blank=True,null=True)
    district=models.CharField(max_length=255, blank=True,null=True)
    upazilla=models.CharField(max_length=255, blank=True,null=True)
    village=models.TextField(max_length=255, blank=True,null=True)
    phoneNumber=models.IntegerField()
    className=models.ForeignKey(StudentClass,on_delete=models.PROTECT)
    studentimage=models.ImageField(upload_to='student_pic')
    blod_groop_choice=(
        ('a+','A+'),
        ('o+','O+'),
        ('b+','B+'),
        ('ab+','AB+'),
        ('a-','A-'),
        ('o-','O-'),
        ('b-','B-'),
        ('ab-','AB+'),        
    )
    blod_groop=models.CharField(choices=blod_groop_choice,max_length=5, blank=True,null=True)
    gender_choice=(
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    )
    gender=models.CharField(choices=gender_choice,max_length=110)
    email=models.EmailField(blank=True,null=True)
    birth_certificate_no=models.IntegerField( blank=True,null=True)
    region_choice=(
        ('Islam', 'Islam'),
        ('Hinduism', 'Hinduism'),
        ('Buddhism', 'Buddhism'),
        ('Christianity', 'Christianity'),
        ('Others', 'Others')
    )
    region=models.CharField(choices=region_choice,max_length=255, blank=True,null=True)
    nationality_choice = (
        ('Bangladeshi', 'Bangladeshi'),
        ('Others', 'Others')
    )
    nationality=models.CharField(choices=nationality_choice,max_length=255, blank=True,null=True)

    def __str__(self):
        return str(self.registration_no)

    
class GuardianInfo(models.Model):
    registration_no=models.IntegerField(primary_key=True)
    father_name=models.CharField(max_length=100)
    father_phone_no=models.CharField(max_length=11, blank=True,null=True)
    father_occupation_choice=(
        ('Agriculture', 'Agriculture'),
        ('Banker', 'Banker'),
        ('Business', 'Business'),
        ('Doctor', 'Doctor'),
        ('Farmer', 'Farmer'),
        ('Fisherman', 'Fisherman'),
        ('Public Service', 'Public Service'),
        ('Private Service', 'Private Service'),
        ('Shopkeeper', 'Shopkeeper'),
        ('Driver', 'Driver'),
        ('Worker', 'Worker'),
        ('N/A', 'N/A'),  
    )
    father_occupation=models.CharField(choices=father_occupation_choice,max_length=45, blank=True,null=True)
    father_yearly_income=models.IntegerField(blank=True,null=True)
    mother_name=models.CharField(max_length=100)
    mother_phone_no=models.CharField(max_length=100, blank=True,null=True)
    mother_ocupation_choice=(   
         ('Agriculture', 'Agriculture'),
        ('Banker', 'Banker'),
        ('Business', 'Business'),
        ('Doctor', 'Doctor'),
        ('Farmer', 'Farmer'),
        ('Fisherman', 'Fisherman'),
        ('Public Service', 'Public Service'),
        ('Private Service', 'Private Service'),
        ('Shopkeeper', 'Shopkeeper'),
        ('Driver', 'Driver'),
        ('Worker', 'Worker'),
        ('House wife', 'House wife'),
        ('N/A', 'N/A'),
    
    )
    mother_ocupation=models.CharField(choices=mother_ocupation_choice,max_length=45, blank=True,null=True)
    mother_yearly_income=models.IntegerField( blank=True,null=True)
    guardian_name=models.CharField(max_length=110, blank=True,null=True)
    guadian_phone_no=models.CharField(max_length=11, blank=True,null=True)
    relationship_choice=(
                ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Brother', 'Brother'),
        ('Uncle', 'Uncle'),
        ('Aunt', 'Aunt'),
    )
    relationship_with_student=models.CharField(choices=relationship_choice,max_length=45, blank=True,null=True)
    
    def __str__(self):
        return self.father_name



class PreviousAcademicInfo(models.Model):
    registration_no=models.IntegerField(primary_key=True)
    institute_name = models.CharField(max_length=100, blank=True,null=True)
    name_of_exam = models.CharField(max_length=100, blank=True,null=True)
    group = models.CharField(max_length=45, blank=True,null=True)
    gpa = models.CharField(max_length=10, blank=True,null=True)
    board_roll = models.IntegerField(blank=True,null=True)
    passing_year = models.IntegerField( blank=True,null=True)

    def __str__(self):
        return str(self.registration_no)



# class AcademicInfo(models.Model): 
#     class_info=models.ForeignKey(StudentClass,on_delete=models.CASCADE)
#     status_select=(('not enroll','Not Enroll'),
#                     ('enrolled','Enrolled'),
#                     ('regular','Regular'),
#                     ('irregular','Irregular'),
#                     ('passed','Passed')
#                     )
#     status=models.CharField(choices=status_select,default='not enroll',max_length=15)
#     emergency_contact_info=models.ForeignKey(EmergencyContactDetails,on_delete=models.CASCADE,null=True)
#     previous_academic_info=models.ForeignKey(PreviousAcademicInfo,on_delete=models.CASCADE,null=True)
#     previous_academic_certificate=models.ForeignKey(PreviousAcademicCerificate,on_delete=models.CASCADE,null=True)
#     date=models.DateField(auto_now_add=True)
#     is_delete=models.BooleanField(default=False)

#     def __str__(self):
#         return str(self.registration_no)

# class EnrolledStudent(models.Model):
#     class_name=models.ForeignKey(ClassInfo,on_delete=models.CASCADE)
#     Student=models.OneToOneField(AcademicInfo,on_delete=models.CASCADE)
#     roll =models.IntegerField()
#     date=models.DateField(auto_now_add=True)

#     class Meta:
#         unique_together=['class_name','roll']

#     def __str__(self):
#         return str(self.roll)

    
