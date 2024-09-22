from django import forms
from .models import LessonCategory, Lesson, VideoContent, TestContent, InputTaskContent, TestOption, Course


class LessonCategoryForm(forms.ModelForm):
    class Meta:
        model = LessonCategory
        fields = ['name', 'description']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['category', 'title', 'description', 'poster']


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'description']


class VideoContentForm(forms.ModelForm):
    class Meta:
        model = VideoContent
        fields = ['lesson', 'video_url', 'duration', 'order']


class TestContentForm(forms.ModelForm):
    class Meta:
        model = TestContent
        fields = ['lesson', 'question', 'order']


class InputTaskContentForm(forms.ModelForm):
    class Meta:
        model = InputTaskContent
        fields = ['lesson', 'task_description', 'correct_answer', 'order']


class TestOptionForm(forms.ModelForm):
    class Meta:
        model = TestOption
        fields = ['test', 'text', 'is_correct']
