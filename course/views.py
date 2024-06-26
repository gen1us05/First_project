from django.shortcuts import render
from django.views import View
from .models import Course, Teacher


class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        context = {
            'courses': courses,
        }
        return render(request, 'main/course.html', context)



class TeacherListView(View):
    def get(self, request):
        teacher = Teacher.objects.all()
        context = {
            'teacher': teacher,
        }
        return render(request, 'main/teacher.html', context)
