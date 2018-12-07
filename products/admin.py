from django.contrib import admin
from products.models import Product, ProductMainCategory, ProductSubCategory
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    models=Product
    readonly_fields=('click_count',)

    list_display=('id','name_en','name_ar','category','main_category','show_home','click_count')
    list_display_links=('id','name_en','name_ar',)

    list_filter=('category__main_category__name_en','category','show_home')

    search_fields=('name_en','name_ar','category__name_en','category__name_ar','category__main_category__name_en','category__main_category__name_ar')

@admin.register(ProductMainCategory)
class ProductMainCategoryAdmin(admin.ModelAdmin):
    models=ProductMainCategory

    list_display=('id','name_en','name_ar','show_home','show_menu','show_footer')
    list_display_links=('id','name_en','name_ar',)
    # actions = None
    # def has_add_permission(self, request):
    #     return False


@admin.register(ProductSubCategory)
class ProductSubCategoryAdmin(admin.ModelAdmin):
    models=ProductSubCategory

    #exclude=('click_count',)
    readonly_fields=('click_count',)

    list_display=('id','name_en','name_ar','main_category','show_home','show_footer','click_count',)
    list_display_links=('id','name_en','name_ar',)
    list_filter=('main_category',)

    # actions = None
    # def has_add_permission(self, request):
    #     return False
