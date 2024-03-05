from django.contrib import admin
from courses.models import Category, Course, Lesson, Tag, Comment, Like
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    list_filter = ['id', 'name', 'created_date']
    search_fields = ['name', 'description']
    readonly_fields = ['avatar']
    form = CourseForm

    def avatar(self, instance):
        if instance:
            return mark_safe(f'<img src="/static/{instance.image.name}" width="120" />')

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

    js = ('/static/js/script.js',)


# admin.site.register(Lesson, LessonAdmin)
admin.site.register(Category)
admin.site.register(Course, MyCourseAdmin)
admin.site.register(Lesson)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Like)