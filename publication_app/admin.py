from django.contrib import admin

# Register your models here.
from publication_app.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    ordering = ('-create_date', '-id', )
    readonly_fields = ("create_date",)
