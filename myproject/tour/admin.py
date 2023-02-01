from django.contrib import admin

from.models import Tour, Author


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('date', 'author', )


admin.site.register(Author)
