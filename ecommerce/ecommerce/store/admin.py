from django.contrib import admin
from .models import Category, Product, Supplier


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }

    fields = ['name', 'slug']


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }

    fields = ['title', 'slug', 'description', 'price', 'image', 'category', 'supplier', 'brand']



class SupplierAdmin(admin.ModelAdmin):
    fields = ['companyname', 'username', 'password']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier, SupplierAdmin)