import pytest

from study.users.models import User
from study.users.tests.factories import UserFactory
from study.lessons.models import Course, Lesson, Exercise
from study.lessons.tests.factories import CourseFactory, LessonFactory, ExerciseFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def course(db) -> Course:
    return CourseFactory()


@pytest.fixture
def course_ten(db) -> list[Course]:
    return CourseFactory.create_batch(size=10, status='published')


@pytest.fixture
def lesson(db) -> Lesson:
    return LessonFactory()


@pytest.fixture
def lesson_ten(db) -> list[Lesson]:
    return LessonFactory.create_batch(size=10, status='published')


@pytest.fixture
def exercise(db) -> Exercise:
    return ExerciseFactory()
