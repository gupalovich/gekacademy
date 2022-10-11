import json

from pprint import pprint
from django.test import RequestFactory
from django.urls import reverse

from study.users.models import User
from ..models import Course, Lesson
from ..api.views import CourseViewSet


class TestCourseViewSet:
    def test_get_queryset(self, course_ten: list[Course], user: User, rf: RequestFactory):
        request = rf.get(reverse('api:course-list'))
        request.user = user
        response = CourseViewSet.as_view({'get': 'list'})(request)
        assert response.status_code == 200
        assert len(response.data) == 10
        assert 'uuid' in response.data[0]

    def test_get_queryset_anon(self, course_ten: list[Course], rf: RequestFactory):
        request = rf.get(reverse('api:course-list'))
        response = CourseViewSet.as_view({'get': 'list'})(request)
        assert response.status_code == 403

    def test_detail(self, course: Course, user: User, rf: RequestFactory):
        request = rf.get(reverse('api:course-detail', kwargs={'uuid': course.uuid}))
        request.user = user
        response = CourseViewSet.as_view({'get': 'retrieve'})(request, uuid=course.uuid)
        # pprint(json.loads(json.dumps(response.data)))
        assert response.status_code == 200
