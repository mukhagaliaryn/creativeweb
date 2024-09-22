from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from progress.models import UserProgress, UserLesson, UserCourse
from workspace.models import LessonCategory, Lesson, Course


# Home page
@login_required(login_url='/accounts/login/')
def home_view(request):
    u_courses = request.user.u_user_courses.all()
    context = {
        'user_profile': request.user,
        'u_courses': u_courses
    }
    return render(request, 'index.html', context)


# Lessons page
@login_required(login_url='/accounts/login/')
def courses_view(request):
    categories = LessonCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'courses/index.html', context)


@login_required(login_url='/accounts/login/')
def course_detail_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {
        'course': course,
    }
    try:
        user_course = UserCourse.objects.get(course=course, user=request.user)
        context = {
            'course': course,
            'user_course': user_course,
            'user_lesson': user_course.uc_user_lessons.all().first()
        }
    except:
        pass

    return render(request, 'courses/course.html', context)


@login_required(login_url='/accounts/login/')
def lesson_detail_view(request, u_course_pk, u_lesson_pk):
    user_course = get_object_or_404(UserCourse, pk=u_course_pk)
    user_lesson = get_object_or_404(UserLesson, pk=u_lesson_pk)
    user_lessons = UserLesson.objects.filter(user_course=user_course)

    context = {
        'user_lesson': user_lesson,
        'user_lessons': user_lessons
    }
    return render(request, 'courses/lesson.html', context)
