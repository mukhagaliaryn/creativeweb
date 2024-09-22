from django.urls import path
from . import views

urlpatterns = [
    path('<course_pk>/', views.start_course, name='start_lesson')
]
