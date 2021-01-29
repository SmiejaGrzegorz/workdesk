from django.contrib import admin
from . import models


class AdminSite(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'title',
        'position_top',
        'position_left',
        'note_box_color',
        'create_date',
    )
    date_hierarchy = 'create_date'


admin.site.register(models.Note, AdminSite)
