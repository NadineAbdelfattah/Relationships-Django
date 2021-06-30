from django.contrib import admin
from .models import Book, Author, Address, Country


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",)
    list_display = ("author", "author",)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address)
admin.site.register(Country)
