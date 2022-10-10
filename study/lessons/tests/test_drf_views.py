from django.test import RequestFactory
from django.urls import reverse

from study.users.models import User
from ..models import Course
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
