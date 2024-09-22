from django.shortcuts import render, redirect

from progress.models import UserCourse, UserLesson
from workspace.models import Course


def start_course(request, course_pk):
    course = Course.objects.get(id=course_pk)
    user = request.user
    lessons = course.lessons.all()

    user_course, created = UserCourse.objects.get_or_create(user=user, course=course)
    for lesson in lessons:
        user_lesson, created = UserLesson.objects.get_or_create(user=user, user_course=user_course, lesson=lesson)

    return redirect('course_detail', course.pk)
