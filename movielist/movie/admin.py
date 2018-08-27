from django.contrib import admin

from .models import Movie
from movielist.core.admin import AuditModelAdmin
# Register your models here.


class MovieAdmin(AuditModelAdmin):
    list_display = (
        'id',
        'title',
        'is_active'
    )

admin.site.register(Movie, MovieAdmin)
