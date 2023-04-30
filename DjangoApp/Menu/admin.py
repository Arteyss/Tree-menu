from django.contrib import admin
from .models import MenuBar, CategoryMenu


class CategoryInLine(admin.TabularInline):
    model = MenuBar
    prepopulated_fields = {"url": ("title",)}


@admin.register(CategoryMenu)
class CategoryMenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (CategoryInLine,)


@admin.register(MenuBar)
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}
    list_display = ('title', 'url', 'parent', 'category')
