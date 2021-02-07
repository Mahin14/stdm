from django.contrib import admin
from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
from django.contrib.auth.admin import UserAdmin
from .models import *
from.forms import *
# Register your models here.
@admin.register(teachers)
@admin.register(students)
class studentAdmin(admin.ModelAdmin):
    search_fields=["registration_no"]
    list_filter=["className"]
    list_display=["first_name"]
    



# if many to many field customije by boolien
# class studentsModelAdmin(admin.ModelAdmin):
#     def render_change_form(self, request, context, *args,**kwargs):
#         context['studentcreateform'].form.fields['className'].queryset=students.objects.filter(is_student=True)
#         return super().render_change_form(self, request, context, *args,**kwargs)





admin.site.register(StudentClass)
admin.site.register(school_notice)





