from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher
from django.core.management import call_command

def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all().prefetch_related('teachers').order_by('group')
    context = {'students': students}
    return render(request, template, context)
