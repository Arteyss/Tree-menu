from django.contrib import admin
from .models import MenuBar, CategoryMenu


@admin.register(MenuBar)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'category')


@admin.register(CategoryMenu)
class CategoryMenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
