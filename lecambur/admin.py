from django.contrib import admin
from .models import Post, Author

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering       = ('-published_date',)
    list_display = ('title', 'published_date', 'topic' )
    
admin.site.register(Post, PostAdmin)
admin.site.register(Author)