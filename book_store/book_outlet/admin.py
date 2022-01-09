from django.contrib import admin

# Register your models here.
from book_outlet.models import Book


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating")
    list_display = ("title", "author")

admin.site.register(Book, BookAdmin)
