

from django.shortcuts import render,redirect

from .models import *
from .forms import *

# Create your views here.
def dashboard(request):
    # user=request.user
    student=students.objects.all()
    teacher=teachers.objects.all()
    class_list=StudentClass.objects.all()
    # print(student['registration_no__count'])
    notice=school_notice.objects.all().order_by('update_date')
    # print(user)
    dict={'notice':notice,'student':student,'class_list':class_list,'teacher':teacher}
    return render(request,'base.html',context=dict)






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

    








def student_list(request):
    student_data=students.objects.all().order_by("-className")
    dict={'students':student_data}
    return render(request,'students/student_list.html',context=dict)

def student_delete(request,id):
    student = students.objects.get(pk=id)
    student.delete()
    return redirect('adminsite:all_student')



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

def all_class(request):
    className=StudentClass.objects.all()
    dict={'className':className}
    
    
    return render(request, "students/class_list.html", context=dict)
    


def class_student_serial(request,classid):
    class_data=students.objects.filter(className_id=classid)
    dict={'students':class_data}
    
    return render(request,"students/class_listSerial.html",context=dict)



def teacher_list(request):
    teachers_data=teachers.objects.all().order_by("positon")
    dict={'teachers':teachers_data}
    return render(request,'teachers/teachers_list.html',context=dict)

def teachers_delete(request,id):
    teacher = teachers.objects.get(pk=id)
    teacher.delete()
    return redirect('adminsite:teacher_list')

    
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
    return render(request,'teachers/teacher_form.html',context=dict)


