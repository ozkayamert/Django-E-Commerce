from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=155)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank= True, null=True)
    is_active = models.BooleanField(default=True)
    seo_title = models.CharField(max_length=155, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=155, unique=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return self.name
    
class Brands(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField(blank=True,null=True)
    seo_title = models.CharField(max_length=155,blank=True,null=True)
    seo_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=155, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    picture = models.ImageField(upload_to="brand-pictures", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Brands"
        verbose_name = "Brand"

    def __str__(self):
        return self.name