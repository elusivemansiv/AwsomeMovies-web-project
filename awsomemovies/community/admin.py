from django.contrib import admin
from .models import Posts

class CommunityPost(admin.ModelAdmin):
    list_display = ('title', 'message', 'slug', 'date')


admin.site.register(Posts, CommunityPost)
