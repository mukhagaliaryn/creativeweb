from django.contrib import admin
from .models import LessonCategory, Lesson, VideoContent, TestContent, InputTaskContent, TestOption, Course


@admin.register(LessonCategory)
class LessonCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at', )
    search_fields = ('title',)


class VideoContentInline(admin.TabularInline):
    model = VideoContent
    extra = 1


class TestContentInline(admin.TabularInline):
    model = TestContent
    extra = 1


class InputTaskContentInline(admin.TabularInline):
    model = InputTaskContent
    extra = 1


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('course',)
    inlines = [VideoContentInline, TestContentInline, InputTaskContentInline]


@admin.register(VideoContent)
class VideoContentAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'video_url', 'duration', )
    list_filter = ('lesson',)


class TestOptionInline(admin.TabularInline):
    model = TestOption
    extra = 2


@admin.register(TestContent)
class TestContentAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'question',)
    list_filter = ('lesson',)
    inlines = [TestOptionInline]


@admin.register(InputTaskContent)
class InputTaskContentAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'task_description', 'correct_answer',)
    list_filter = ('lesson',)
