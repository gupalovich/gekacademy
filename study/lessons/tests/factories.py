from factory import Faker
from factory.fuzzy import FuzzyChoice
from factory.django import DjangoModelFactory

from ..models import Course, Lesson, Exercise


class CourseFactory(DjangoModelFactory):
    title = Faker('name')
    status = FuzzyChoice(choices=['draft', 'published'])

    class Meta:
        model = Course
        django_get_or_create = ['title']
