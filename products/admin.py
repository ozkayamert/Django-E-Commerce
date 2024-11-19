from django.contrib import admin
from .models import Categories, Brands, Products, Tags

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'seo_title', 'slug', 'is_active']
    list_filter = ['is_active', 'name']
    search_fields = ['name', 'seo_title', 'slug']

admin.site.register(Categories, CategoryAdmin)


class BrandsAdmin(admin.ModelAdmin):
    list_display = ['name','seo_title','slug','is_active','picture']
    list_filter = ['is_active','name']
    search_fields = ['name','seo_title','slug']

admin.site.register(Brands,BrandsAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','brand','category','discount_price','is_active','image','date']
    list_filter = ['is_active','name','category','brand']
    search_fields = ['name','seo_title','slug']

admin.site.register(Products, ProductAdmin)

admin.site.register(Tags)