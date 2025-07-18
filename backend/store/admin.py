from django.contrib import admin
from store.models import Category, Product, Gallery, Specification, Color, Size, Cart, CartOrder, CartOrderItem,Review

# Register your models here.
# // we want this model to show in Product
class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1


class SpecificationInline(admin.TabularInline):
    model = Specification
    extra = 1


class ColorInline(admin.TabularInline):
    model = Color
    extra = 1


class SizeInline(admin.TabularInline):
    model = Size
    extra = 1




class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'vendor', 'featured']
    list_editable = ['featured']
    list_filter = ['date']
    search_fields = ['title']

    inlines = [GalleryInline, SpecificationInline, ColorInline, SizeInline]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

admin.site.register(Cart)
admin.site.register(CartOrder)
admin.site.register(CartOrderItem)
admin.site.register(Review, ReviewAdmin)




