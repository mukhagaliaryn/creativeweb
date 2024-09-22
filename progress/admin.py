from django.contrib import admin
from .models import UserCourse, UserLesson


class UserLessonTable(admin.TabularInline):
    model = UserLesson
    extra = 0


class UserCourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'is_completed', )
    list_filter = ('user', 'course', 'is_completed', )
    search_fields = ('course', 'user', )

    inlines = [UserLessonTable]


admin.site.register(UserCourse, UserCourseAdmin)

