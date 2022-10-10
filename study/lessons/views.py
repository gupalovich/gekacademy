from django.shortcuts import render
from django.views.generic import ListView

from .models import Lesson


class CourseView(ListView):
    model = Lesson
