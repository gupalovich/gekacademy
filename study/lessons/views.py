from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Course, Lesson, Exercise


class CourseView(DetailView):
    model = Course


class LessonView(ListView):
    model = Lesson
