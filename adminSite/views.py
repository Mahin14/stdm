
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Count
from django.shortcuts import get_object_or_404, render,redirect

from .models import *
from .forms import *
from .filter import *

@login_required
def dashboard(request):
    # user=request.user
    student = students.objects.all().count()
    
    print(student)
    teacher = students.objects.all().count()
    
    print(teacher)
    class_list=StudentClass.objects.all()
    # print(student['registration_no__count'])
    notice=school_notice.objects.all().order_by('update_date')
    # print(user)
    dict={'notice':notice,'student':student,'class_list':class_list,'teacher':teacher}
    print(dict)
    return render(request,'dashboard.html',context=dict)





@login_required
def student_form(request, id=0):
    if request.method =="GET":
        if id==0:
            form=studentcreateform()
        else:
            stm=students.objects.get(pk=id)
            form=studentcreateform(instance=stm)
        dict={'form':form}
        return render(request,'students/student_form.html',context=dict)
    else:
        if id==0:
            form=studentcreateform(request.POST,request.FILES)
        else:
            stm=students.objects.get(pk=id)
            form=studentcreateform(instance=stm)
        if form.is_valid():
            form.save()
        return redirect('adminsite:all_student')


    

@login_required
def teacher_form(request, id=0):
    if request.method =="GET":
        if id==0:
            form=teacherCreationform()
        else:
            stm=teachers.objects.get(pk=id)
            form=teacherCreationform(instance=stm)
        dict={'form':form}
        return render(request,'teachers/teacher_form.html',context=dict)
    else:
        if id==0:
            form=teacherCreationform(request.POST,request.FILES)
        else:
            stm=teachers.objects.get(pk=id)
            form=teacherCreationform(instance=stm)
        if form.is_valid():
            form.save()
        return redirect('adminsite:teacher_list')

    







@login_required
def student_list(request):
    student_data=students.objects.all()
    register_no=request.POST.get('registration_no')
    if register_no !="" and register_no is not None:
        student_data=student_data.filter(registration_no__icontains=register_no)
    dict={'students':student_data}
    return render(request,'students/student_list.html',context=dict)



@login_required
def student_delete(request,id):
    student = StudentClass.objects.get(pk=id)
    student.delete()
    return redirect('adminsite:all_class')


@login_required
def create_class(request,id=0):
    if request.method =="GET":
        if id==0:
            form=studentclasscreate()
        else:
            stc=StudentClass.objects.get(pk=id)
            form=studentclasscreate(instance=stc)            

        return render(request, "students/create_class.html", context={'form': form})
        
    else:
        if id==0:
            form=studentclasscreate(request.POST)

        else:
            stc=StudentClass.objects.get(pk=id)
            form=studentclasscreate(request.POST,instance=stc)
        if form.is_valid():
            form.save()
        return redirect('adminsite:all_class')


@login_required
def all_class(request):
    className=StudentClass.objects.all()
    dict={'className':className}
    
    
    return render(request, "students/class_list.html", context=dict)
    

@login_required
def class_student_serial(request,classid):
    class_data=students.objects.filter(className_id=classid)
    dict={'students':class_data}
    
    return render(request,"students/class_listSerial.html",context=dict)


@login_required
def teacher_list(request):
    teachers_data=teachers.objects.all().order_by("positon")
    dict={'teachers':teachers_data}
    return render(request,'teachers/teachers_list.html',context=dict)


@login_required
def teachers_delete(request,id):
    teacher = teachers.objects.get(pk=id)
    teacher.delete()
    return redirect('adminsite:teacher_list')

@login_required  
def create_Notice(request):
    heading='create notice'
    form=CreteNotice()
    if request.method=='POST':
        form=CreteNotice(request.POST)
        if form.is_valid:
            form_obj=form.save(commit=False)
            user=request.user
            form_obj.created_by=user
            form_obj.save()
            return redirect('adminsite:dashboard')
    dict={'form':form,'heading':heading}
    return render(request,'students/create_notice.html',context=dict)

def login_page(request):
    return render(request,'login.html',context={})


def user_login(request):
    # if request.method=='GET':
    #     return render(request,'login.html')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(username=username,password=password)
        if user:
            # if user.is_superuser:
            if user.is_active:
                login(request,user)
                return redirect('adminsite:dashboard')
        else:
            messages="user does not exist"
            return render(request,'login.html',{'messages':messages})

    else:
        return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('adminsite:login')

@login_required
def studentDetails(request,id):
    student_data=get_object_or_404(students,pk=id)
    dict={'student':student_data}

    return render(request,'students/studentDetails.html',context=dict)