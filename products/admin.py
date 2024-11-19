from django.contrib import admin
from .models import Categories, Brands

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