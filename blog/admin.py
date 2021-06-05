from django.contrib import admin

from .models import BlogPost, Author, Tag, Address, Comment


# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("title", "author")
    list_display = ("title", "date", "author",)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "comment")


admin.site.register(BlogPost, BlogPostAdmin)

admin.site.register(Author)

admin.site.register(Tag)

admin.site.register(Address)

admin.site.register(Comment, CommentAdmin)
