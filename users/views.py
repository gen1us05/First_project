from django.shortcuts import render
from django.views import View
from course.models import Course, Speciality, Teacher


class LandingPageView(View):
    def get(self, request):
        specialitys = Speciality.objects.all()
        courses = Course.objects.all()
        teachers = Teacher.objects.all()
        context = {
            'specialitys': specialitys,
            'courses': courses,
            'teachers': teachers,
        }
        return render(request, 'main/index.html', context)
