

from django.urls import path
from .views import *

app_name='adminsite'


urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('createstudent',student_form,name='student_creation'),
    path('updatestudent/<int:id>',student_form,name='student_update'),
    path('deleteStudent/<int:id>',student_delete,name='student_delete'),
    path('studentlist',student_list,name='all_student'),
    
    # class url
    path('createclasss',create_class,name='class_creation'),
    path('updateclass/<int:id>',create_class,name='class_update'),
    path('deleteclass/<int:id>',student_delete,name='class_delete'),
    path('classList',all_class,name='all_class'),
    path('classListStudentSerial/<str:classid>',class_student_serial,name='student_serial'),

    # teacher url
    path('teacherList',teacher_list,name='teacher_list'),
    path('create_teacher',teacher_form,name='teacher_create'),
    path('update_teacher/<int:id>',teacher_form,name='update_teacher'),
    path('deleteTeacher/<int:id>',teachers_delete,name='teacher_delete'),

    # notice url
    path('Create_notice',create_Notice,name='create_notice'),

    #login page
    path('user_login',user_login,name='user_login'),
    path('login',login_page,name='login'),
    path('logout',user_logout,name='logout')

    

    #     path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    # path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    # path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
   

]