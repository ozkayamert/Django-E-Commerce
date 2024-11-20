from django.db import models
from django.contrib.auth.models import User

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
    
class Tags(models.Model):
    name = models.CharField(max_length=155)
    slug = models.SlugField(max_length=155,unique=True,null=True,blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Tags'
        verbose_name = 'Tag'

    def __str__(self):
        return self.name

    
class Products(models.Model):
    name = models.CharField(max_length=155)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    brand = models.ForeignKey(Brands,on_delete=models.CASCADE)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    discount_price = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    short_description = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    seo_title = models.CharField(max_length=155,blank=True,null=True)
    seo_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=155, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="productimages",blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tags,blank=True)
    home = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'

    def __str__(self):
        return self.name