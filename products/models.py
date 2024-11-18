from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=155)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return self.name