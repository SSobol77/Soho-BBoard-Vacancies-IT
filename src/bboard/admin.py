from django.contrib import admin
from .models import Bb, Rubric


# Register your models here.

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content', 'rubric')
    search_fields = ('title', 'content', 'rubric')


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
