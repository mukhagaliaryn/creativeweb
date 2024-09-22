from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('courses/', views.courses_view, name='courses'),
    path('course/<pk>/', views.course_detail_view, name='course_detail'),
    path('user/course/<u_course_pk>/lesson/<u_lesson_pk>/', views.lesson_detail_view, name='lesson_detail')
]
