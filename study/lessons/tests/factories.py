from factory import SubFactory, Faker, post_generation
from factory.fuzzy import FuzzyChoice
from factory.django import DjangoModelFactory

from ..models import Course, Lesson, Exercise


class CourseFactory(DjangoModelFactory):
    title = Faker('name', locale='ru_RU')
    status = FuzzyChoice(choices=['draft', 'published'])

    class Meta:
        model = Course
        django_get_or_create = ['title']


class LessonFactory(DjangoModelFactory):
    title = Faker('name', locale='ru_RU')
    theory = Faker('name')
    status = FuzzyChoice(choices=['draft', 'published'])
    course = SubFactory(CourseFactory)

    class Meta:
        model = Lesson
        django_get_or_create = ['title']
