from django.contrib import admin
from .models import Institution, Faculty, Department, Program

# Register your models here.

class FacultyInline(admin.TabularInline):
    model = Faculty
    extra = 1

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }
    inlines = [FacultyInline]
    fields = ('name', 'slug', 'phone', 'email', 'website', 'description')
    list_display = ('id', 'name', 'phone', 'email', 'website','created_at','updated_at')
    list_editable = ('name', 'email', 'website')
    search_fields = ('name','website')


class DepartmentInline(admin.TabularInline):
    model = Department
    extra = 2
    min_num = 1 # minimum number of required department in a faculty


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    inlines = [DepartmentInline]

    fields = ('name','institution','dean','email','description')
    list_display = ('id','name','institution','dean','email')
    list_editable = ('name','institution','dean','email')


class ProgramInline(admin.TabularInline):
    model = Program
    min_num = 1
    extra = 1


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    inlines = [ProgramInline]
    fields = ('name','faculty','head_of_department','email','description')
    list_display = ('id','name','faculty','head_of_department','email')
    list_editable = ('name','faculty','head_of_department','email')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    fields = ('degree_type','duration','duration_type','department')
    list_display = ('id','degree_type','duration','duration_type','department')
    list_editable = ('degree_type','duration','duration_type')

