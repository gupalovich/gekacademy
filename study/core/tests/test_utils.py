import pytest

from transliterate import translit

from study.lessons.models import Course
from ..utils import (
    capitalize_str,
    capitalize_slug,
)
from .factories import model_slug_test_generator


@pytest.mark.django_db
def test_get_unique_slug() -> None:
    """Test unique slug generation; conversion to ru locale"""
    test_slugs = [
        'some @ long giberish-dsfgsdfg!',
        translit('тест @ заголовок!', 'ru', reversed=True),  # test-zagolovok
    ]
    for test_slug in test_slugs:
        model_slug_test_generator(Course, test_slug)


def test_capitalize_str() -> None:
    test_strings = [
        ('test title', 'Test Title'),
        ('test-zagolovok', 'Test-zagolovok'),
        ('тест @ заголовок!', 'Тест @ Заголовок!')]
    for s, result in test_strings:
        func_res = capitalize_str(s)
        assert func_res == result


def test_capitalize_slug() -> None:
    test_slugs = [
        ('test-title', 'Test Title'),
        ('test-zagolovok', 'Test Zagolovok'),
        ('test-zagolovok-1', 'Test Zagolovok'),
    ]
    for s, result in test_slugs:
        func_res = capitalize_slug(s)
        assert func_res == result
