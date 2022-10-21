import pytest

from gekacademy.users.models import User
from gekacademy.users.tests.factories import UserFactory
from gekacademy.lessons.models import Course, Lesson, Exercise, Achievement
from gekacademy.lessons.tests.factories import (
    CourseFactory,
    LessonFactory,
    ExerciseFactory,
    AchievementFactory,
)


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
    return CourseFactory.create_batch(size=10)


@pytest.fixture
def lesson(db) -> Lesson:
    return LessonFactory()


@pytest.fixture
def lesson_ten(db) -> list[Lesson]:
    return LessonFactory.create_batch(size=10)


@pytest.fixture
def exercise(db) -> Exercise:
    return ExerciseFactory()


@pytest.fixture
def exercise_ten(db) -> list[Exercise]:
    return ExerciseFactory.create_batch(size=10)


@pytest.fixture
def achievement(db) -> Achievement:
    return AchievementFactory()
