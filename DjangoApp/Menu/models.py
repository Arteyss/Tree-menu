from django.db import models


class CategoryMenu(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MenuBar(models.Model):
    title = models.CharField(max_length=50)
    url = models.SlugField(unique=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.CASCADE,
        )
    category = models.ForeignKey(
        CategoryMenu,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.title
