from django.contrib import admin
from . import models


class BlogAdmin(admin.ModelAdmin):
    list_display = ("id","title", "summary", "slug")
    list_display_links = ("id", "title")
    # list_filter = ("title",) # admin panelindeki veri tabanında filtreleme sağlar
    search_fields = ("title", "text")
    list_per_page = 40 # default 30 

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name", "slug", "blog_count")
    list_display_links = ("id", "name")

    # O kategoriye ait kaç tane blog yazısı var
    def blog_count(self, obj):
        return obj.blog_set.count()





# Register your models here.
admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.BlogCategory, BlogCategoryAdmin)