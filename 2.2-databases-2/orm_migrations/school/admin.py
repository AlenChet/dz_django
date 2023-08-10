from django.contrib import admin
from .models import Student, Teacher

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'display_teachers')
    filter_horizontal = ('teachers',)

    def display_teachers(self, obj):
        return ", ".join([teacher.name for teacher in obj.teachers.all()])

    display_teachers.short_description = 'Преподаватели'

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)