from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from apps.models import Category, Product, ProductImage, Review, Tag


@admin.register(Category)
class CategoryDraggableMPTTAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImage
    min_num = 0
    extra = 2


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = [ProductImageStackedInline]


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    pass
