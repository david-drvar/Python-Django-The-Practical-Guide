from django.contrib import admin

# Register your models here.
from book_outlet.models import Book, Author, Address


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating")
    list_display = ("title", "author")


class AuthorAdmin(admin.ModelAdmin):
    # list_filter = ("author", "rating")
    list_display = ("first_name", "last_name")


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address)
