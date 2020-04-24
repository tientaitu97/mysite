from django.contrib import admin

# Register your models here.
from blog.models import Post, Profile, Images, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'status')
    list_filter = ('status', 'created', 'updated')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'photo')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'content', 'timestamp')


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Images, ImageAdmin)
admin.site.register(Comment, CommentAdmin)