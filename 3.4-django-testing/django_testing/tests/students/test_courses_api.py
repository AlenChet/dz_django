import pytest
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def course_factory():
    def create_course(**kwargs):
        return baker.make('students.Course', **kwargs)

    return create_course

@pytest.fixture
def student_factory():
    def create_student(**kwargs):
        return baker.make('students.Student', **kwargs)

    return create_student

@pytest.mark.django_db
def test_retrieve_course(api_client, course_factory):
    course = course_factory()
    url = reverse('course-detail', kwargs={'pk': course.pk})
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == course.pk

@pytest.mark.django_db
def test_list_courses(api_client, course_factory):
    course1 = course_factory()
    course2 = course_factory()
    url = reverse('course-list')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['id'] == course1.pk
    assert response.data[1]['id'] == course2.pk

@pytest.mark.django_db
def test_filter_courses_id(api_client, course_factory):
    course1 = course_factory()
    course2 = course_factory()
    url = reverse('course-list') + '?id=' + str(course1.pk)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['id'] == course1.pk

@pytest.mark.django_db
def test_filter_courses_name(api_client, course_factory):
    course1 = course_factory(name='Python')
    course2 = course_factory(name='Django')
    url = reverse('course-list') + '?name=Python'
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Python'

@pytest.mark.django_db
def test_create_course(api_client):
    data = {
        'name': 'Python',
        'students': []
    }
    url = reverse("course-list")
    response = api_client.post(url, data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'Python'

@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    course = course_factory()
    data = {
        'name': 'fullstack-разраб Python',
        'students': []
    }
    url = reverse('course-detail', kwargs={'pk': course.pk})
    response = api_client.put(url, data)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'fullstack-разраб Python'

@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    course = course_factory()
    url = reverse('course-detail', kwargs={'pk': course.pk})
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT

