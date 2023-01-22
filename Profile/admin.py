from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Skill)
admin.site.register(UserProfile)
admin.site.register(Aboutprofile)
admin.site.register(Certificate)
admin.site.register(Portfolio)
admin.site.register(ProjectWork)
admin.site.register(ExperienceWork)
admin.site.register(ContactProfile)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BlogPage, PostAdmin)

admin.site.register(Achievement)
