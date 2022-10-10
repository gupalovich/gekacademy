from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Course, Lesson, Exercise


class CourseListView(ListView):
    model = Course


class LessonListView(ListView):
    model = Lesson


class ExerciseDetailView(DetailView):
    model = Exercise
