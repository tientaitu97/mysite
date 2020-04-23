from django.contrib import admin

# Register your models here.
from blog.models import Post, Profile


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'status')
    list_filter = ('status', 'created', 'updated')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'photo')


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
