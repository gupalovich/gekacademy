import json
import uuid as uuid_lib

from pprint import pprint
from django.test import RequestFactory
from django.urls import reverse

from study.users.models import User
from ..models import Course, Lesson, Exercise
from ..api.views import CourseViewSet, LessonViewSet, ExerciseViewSet
from .factories import LessonFactory, ExerciseFactory


class TestCourseViewSet:
    def test_get_queryset(self, course_ten: list[Course], user: User, rf: RequestFactory):
        """Тест ответа для course-list"""
        request = rf.get(reverse('api:course-list'))
        request.user = user
        response = CourseViewSet.as_view({'get': 'list'})(request)
        assert response.status_code == 200
        assert len(response.data) == 10
        assert 'uuid' in response.data[0]

    def test_get_queryset_anon(self, course_ten: list[Course], rf: RequestFactory):
        """Тест ответа для course-list anon user"""
        request = rf.get(reverse('api:course-list'))
        response = CourseViewSet.as_view({'get': 'list'})(request)
        assert response.status_code == 403

    def test_detail(self, course: Course, user: User, rf: RequestFactory):
        """Тест ответа для course-detail"""
        uuid = course.uuid
        request = rf.get(reverse('api:course-detail', kwargs={'uuid': uuid}))
        request.user = user
        response = CourseViewSet.as_view({'get': 'retrieve'})(request, uuid=uuid)
        assert response.status_code == 200

    def test_detail_404(self, course: Course, user: User, rf: RequestFactory):
        """Тест ответа для course-detail 404 страницы"""
        uuid = uuid_lib.uuid4()
        request = rf.get(reverse('api:course-detail', kwargs={'uuid': uuid}))
        request.user = user
        response = CourseViewSet.as_view({'get': 'retrieve'})(request, uuid=uuid)
        assert response.status_code == 404

    def test_lessons(self, course: Course, user: User, rf: RequestFactory):
        """"Тест ответа для course-lessons
           Создать {batch_size} lessons, проверить ответ/данные
           To_dict: pprint(json.loads(json.dumps(response.data)))
        """
        uuid = course.uuid
        batch_size = 5
        # create {batch_size} lessons
        [LessonFactory(course=course) for i in range(batch_size)]
        # build request
        request = rf.get(reverse('api:course-lessons', kwargs={'uuid': uuid}))
        # set user auth
        request.user = user
        response = CourseViewSet.as_view({'get': 'lessons'})(request, uuid=uuid)
        assert response.status_code == 200
        assert len(response.data) == batch_size

    def test_lessons_404(self, course: Course, user: User, rf: RequestFactory):
        """Тест ответа для course-lessons 404 страницы"""
        uuid = uuid_lib.uuid4()
        request = rf.get(reverse('api:course-lessons', kwargs={'uuid': uuid}))
        request.user = user
        response = CourseViewSet.as_view({'get': 'lessons'})(request, uuid=uuid)
        assert response.status_code == 404


class TestLessonViewSet:
    def test_get_queryset(self, lesson_ten: list[Lesson], user: User, rf: RequestFactory):
        """Тест ответа для lesson-list"""
        request = rf.get(reverse('api:lesson-list'))
        request.user = user
        response = LessonViewSet.as_view({'get': 'list'})(request)
        assert response.status_code == 200
        assert len(response.data) == 10
        assert 'uuid' in response.data[0]

    def test_get_queryset_anon(self, lesson_ten: list[Lesson], rf: RequestFactory):
        """Тест ответа для lesson-list anon user"""
        request = rf.get(reverse('api:lesson-list'))
        response = LessonViewSet.as_view({'get': 'list'})(request)
        assert response.status_code == 403

    def test_detail(self, lesson: Lesson, user: User, rf: RequestFactory):
        """Тест ответа для lesson-detail"""
        uuid = lesson.uuid
        request = rf.get(reverse('api:lesson-detail', kwargs={'uuid': uuid}))
        request.user = user
        response = LessonViewSet.as_view({'get': 'retrieve'})(request, uuid=uuid)
        # pprint(json.loads(json.dumps(response.data)))
        assert response.status_code == 200

    def test_detail_404(self, lesson: Lesson, user: User, rf: RequestFactory):
        """Тест ответа для lesson-detail"""
        uuid = uuid_lib.uuid4()
        request = rf.get(reverse('api:lesson-detail', kwargs={'uuid': uuid}))
        request.user = user
        response = LessonViewSet.as_view({'get': 'retrieve'})(request, uuid=uuid)
        assert response.status_code == 404

    def test_exercises(self, lesson: Lesson, user: User, rf: RequestFactory):
        """"Тест ответа для lesson-exercises
           Создать {batch_size} exercises, проверить ответ/данные
           To_dict: pprint(json.loads(json.dumps(response.data)))
        """
        uuid = lesson.uuid
        batch_size = 5
        # create {batch_size} lessons
        [ExerciseFactory(lesson=lesson) for i in range(batch_size)]
        # build request
        request = rf.get(reverse('api:lesson-exercises', kwargs={'uuid': uuid}))
        # set user auth
        request.user = user
        response = LessonViewSet.as_view({'get': 'exercises'})(request, uuid=uuid)
        # pprint(json.loads(json.dumps(response.data)))
        assert response.status_code == 200
        assert len(response.data) == batch_size

    def test_exercises_404(self, lesson: Lesson, user: User, rf: RequestFactory):
        """"Тест ответа для lesson-exercises
           Создать {batch_size} exercises, проверить ответ/данные
           To_dict: pprint(json.loads(json.dumps(response.data)))
        """
        uuid = uuid_lib.uuid4()
        request = rf.get(reverse('api:lesson-exercises', kwargs={'uuid': uuid}))
        request.user = user
        response = LessonViewSet.as_view({'get': 'exercises'})(request, uuid=uuid)
        assert response.status_code == 404


class TestExerciseViewSet:
    def test_get_queryset(self, exercise_ten: list[Exercise], user: User, rf: RequestFactory):
        """Тест ответа для exercise-list"""
        request = rf.get(reverse('api:exercise-list'))
        request.user = user
        response = ExerciseViewSet.as_view({'get': 'list'})(request)
        assert response.status_code == 200
        assert len(response.data) == 10
        assert 'uuid' in response.data[0]

    def test_get_queryset_anon(self, exercise_ten: list[Exercise], rf: RequestFactory):
        """Тест ответа для exercise-list anon user"""
        request = rf.get(reverse('api:exercise-list'))
        response = ExerciseViewSet.as_view({'get': 'list'})(request)
        assert response.status_code == 403

    def test_detail(self, exercise: Exercise, user: User, rf: RequestFactory):
        """Тест ответа для exercise-detail"""
        uuid = exercise.uuid
        request = rf.get(reverse('api:exercise-detail', kwargs={'uuid': uuid}))
        request.user = user
        response = ExerciseViewSet.as_view({'get': 'retrieve'})(request, uuid=uuid)
        # pprint(json.loads(json.dumps(response.data)))
        assert response.status_code == 200

    def test_detail_404(self, exercise: Exercise, user: User, rf: RequestFactory):
        """Тест ответа для exercise-detail"""
        uuid = uuid_lib.uuid4()
        request = rf.get(reverse('api:exercise-detail', kwargs={'uuid': uuid}))
        request.user = user
        response = ExerciseViewSet.as_view({'get': 'retrieve'})(request, uuid=uuid)
        assert response.status_code == 404
