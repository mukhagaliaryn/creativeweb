from django.db import models
from django.utils.translation import gettext_lazy as _


class LessonCategory(models.Model):
    name = models.CharField(_('Название'), max_length=255, unique=True)
    description = models.TextField(_('Описание'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категорий')


class Course(models.Model):
    category = models.ForeignKey(
        LessonCategory, related_name='courses', on_delete=models.CASCADE,
        verbose_name=_('Категория')
    )
    title = models.CharField(_('Название'), max_length=255)
    description = models.TextField(_('Описание'), blank=True, null=True)
    poster = models.ImageField(upload_to='courses/posters/', blank=True, null=True)
    created_at = models.DateTimeField(_('Создано'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Обновлено'), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Курс')
        verbose_name_plural = _('Курсы')


class Lesson(models.Model):
    course = models.ForeignKey(
        Course, related_name='lessons', on_delete=models.CASCADE,
        verbose_name=_('Курс')
    )
    title = models.CharField(_('Заглавие'), max_length=255)
    description = models.TextField(_('Описание'), blank=True, null=True)
    created_at = models.DateTimeField(_('Создано'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Обновлено'), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Урок')
        verbose_name_plural = _('Уроки')


class LessonContent(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='contents', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(_('Порядок'), default=0)

    class Meta:
        abstract = True
        ordering = ['order']

    def __str__(self):
        return f'Content for {self.lesson.title}'


class VideoContent(LessonContent):
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE,
        related_name='video_contents', verbose_name=_('Урок')
    )
    video_url = models.URLField(_('Видео URL'), max_length=500)
    duration = models.DurationField(_('Продолжительность'))

    class Meta:
        verbose_name = _('Видеоконтент')
        verbose_name_plural = _('Видеоконтент')

    def __str__(self):
        return f'Видео: {self.video_url} (Урок: {self.lesson.title})'


class TestContent(LessonContent):
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE,
        related_name='test_contents', verbose_name=_('Урок')
    )
    question = models.TextField(_('Вопрос'), max_length=500)

    class Meta:
        verbose_name = _('Тестконтент')
        verbose_name_plural = _('Тестконтенты')

    def __str__(self):
        return f'Тест: {self.question} (Урок: {self.lesson.title})'


class TestOption(models.Model):
    test = models.ForeignKey(
        TestContent, related_name='options', on_delete=models.CASCADE,
        verbose_name=_('Tест')
    )
    text = models.TextField(_('Текст'), max_length=255)
    is_correct = models.BooleanField(_('Является правильным'), default=False)

    def __str__(self):
        return f'Вариант: {self.text} (Правильно: {self.is_correct})'


class InputTaskContent(LessonContent):
    lesson = models.ForeignKey(
        Lesson, related_name='input_task_contents', on_delete=models.CASCADE,
        verbose_name=_('Урок')
    )
    task_description = models.TextField(_('Описание задачи'))
    correct_answer = models.CharField(_('Является правильным'), max_length=255)

    class Meta:
        verbose_name = _('Ввод содержимого задачи')
        verbose_name_plural = _('Ввод содержимого задачи')

    def __str__(self):
        return f'Входная задача: {self.task_description} (Урок: {self.lesson.title})'
