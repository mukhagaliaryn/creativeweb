from django.db import models
from accounts.models import User
from workspace.models import Lesson, Course
from django.utils.translation import gettext_lazy as _


class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='user_progress')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='user_progress')
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)

    test_score = models.IntegerField(null=True, blank=True)
    task_result = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'lesson')

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title}: {'Завершено' if self.completed else 'Не завершено'}"


class UserCourse(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='u_user_courses', verbose_name=_('Пользователь')
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE,
        related_name='c_user_courses', verbose_name=_('Курс')
    )
    is_completed = models.BooleanField(_('Is_completed'), default=False)

    def __str__(self):
        return '{}: {}'.format(self.user, self.course.title)

    class Meta:
        verbose_name = _('Пользователь курс')
        verbose_name_plural = _('Пользователь курсы')


class UserLesson(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='u_user_lessons', verbose_name=_('Пользователь')
    )
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE,
        related_name='l_user_lessons', verbose_name=_('Урок')
    )
    user_course = models.ForeignKey(
        UserCourse, on_delete=models.CASCADE,
        related_name='uc_user_lessons', verbose_name=_('Пользователь курс')
    )
    is_completed = models.BooleanField(_('Is_completed'), default=False)

    def __str__(self):
        return '{}: {}'.format(self.user, self.lesson)

    class Meta:
        verbose_name = _('Пользователь урок')
        verbose_name_plural = _('Пользователь уроки')
