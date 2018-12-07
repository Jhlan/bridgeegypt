from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

# ProductMainCategory Model
class ProductMainCategory(models.Model):
    name_ar=models.CharField(_('main category in arabic'),max_length=100,blank=True)
    name_en=models.CharField(_('main category in english'),max_length=100,blank=True)

    description_ar=models.TextField(_('description in arabic'),max_length=1000,blank=True)
    description_en=models.TextField(_('description in english'),max_length=1000,blank=True)

    cycle_inner_ar=models.TextField(_('Inner data in arabic'),max_length=1000,blank=True)
    cycle_inner_en=models.TextField(_('Inner data  in english'),max_length=1000,blank=True)

    choices=(
        ('y','Yes'),
        ('n','No'),
    )

    show_menu=models.CharField(_('Show in menu'),help_text=_('Show Main category in Main menu'),default='y',max_length=1,choices=choices)
    show_home=models.CharField(_('Show in home'),help_text=_('Show Main category in homepage'),default='y',max_length=1,choices=choices)
    show_footer=models.CharField(_('Show in footer'),help_text=_('Show Main category in footer'),default='y',max_length=1,choices=choices)

    class Meta:
        verbose_name='Main Category'
        verbose_name_plural='Main Categories'

    def __str__(self):
        return f'{self.name_en}'


# ProductSubCategory Model
class ProductSubCategory(models.Model):

    main_category=models.ForeignKey(ProductMainCategory, on_delete=models.SET_NULL,verbose_name=_('main category name'), help_text=_('Choose Main Category Name'), null=True, blank=True)

    name_ar=models.CharField(_('sub category in arabic'),max_length=100,blank=True)
    name_en=models.CharField(_('sub category in english'),max_length=100,blank=True)

    description_ar=models.TextField(_('description in arabic'),max_length=1000,blank=True)
    description_en=models.TextField(_('description in english'),max_length=1000,blank=True)

    click_count=models.IntegerField(_('times of click'),default=0,null=True, blank=True)

    choices=(
        ('y','Yes'),
        ('n','No'),
    )
    show_home=models.CharField(_('Show in home'),help_text=_('Show Subcategory in homepage'),default='y',max_length=1,choices=choices)
    show_footer=models.CharField(_('Show in footer'),help_text=_('Show Subcategory in footer'),default='y',max_length=1,choices=choices)


    class Meta:
        verbose_name='Subcategory'
        verbose_name_plural='Subcategories'

    def __str__(self):
        return f'{self.name_en}'




# Product Model
class Product(models.Model):

    category=models.ForeignKey(ProductSubCategory, on_delete=models.SET_NULL,verbose_name=_('Subcategory'), help_text=_('Choose Subcategory Name'), null=True, blank=True)

    name_ar=models.CharField(_('name in arabic '),max_length=50,help_text=_("Product Name in Arabic"))
    name_en=models.CharField(_('name in english'),max_length=50,help_text=_("Product Name in English"))

    description_ar=models.TextField(_('description in arabic'),max_length=1000,help_text=_("Product Description in Arabic"))
    description_en=models.TextField(_('description in english'),max_length=1000,help_text=_("Product Description in English"))
    photo = models.ImageField(upload_to='products/')
    click_count=models.IntegerField(_('times of click'), default=0,null=True, blank=True)
    choices=(
        ('y','Yes'),
        ('n','No'),
    )
    show_home=models.CharField(_('Show'),help_text=_('Show the Prdouct in homepage'),default='y',max_length=1,choices=choices)

    detail_ar=RichTextUploadingField(_('detail in arabic'),help_text=_("Product Detail in Arabic"),blank=True)
    detail_en=RichTextUploadingField(_('detail in english'),help_text=_("Product Detail in English"),blank=True)

    material_ar=models.CharField(_('material in arabic'),max_length=50,help_text=_("Material in Arabic"),blank=True)
    material_en=models.CharField(_('material in english'),max_length=50,help_text=_("Material in English"),blank=True)

    keywords_ar=models.TextField(_('keywords in arabic'),max_length=1000,help_text=_("Product keywords in Arabic"),blank=True)
    keywords_en=models.TextField(_('keywords in english'),max_length=1000,help_text=_("Product keywords in English"),blank=True)

    length= models.CharField(_('length'), max_length=50, help_text=_('Product Length'), null=True, blank=True)
    width = models.CharField(_('width'),  max_length=50, help_text=_('Product Width'), null=True, blank=True)
    height= models.CharField(_('height'), max_length=50, help_text=_('Product Height'), null=True, blank=True)
    weight= models.CharField(_('weight'),max_length=50,help_text=_('Product Weight'), null=True, blank=True)
    thickness= models.CharField(_('thickness'),max_length=50,help_text=_('Product Thickness'), null=True, blank=True)
    density= models.CharField(_('density'),max_length=50,help_text=_('Product Density'), null=True, blank=True)
    ref=models.CharField(_('product code'),max_length=50,help_text=_("Product Code"),blank=True)



    class Meta:
        verbose_name=_('Product')
        verbose_name_plural=_('Products')

    def __str__(self):
        return f'{self.name_en}'


    def sub_category(self):
        return self.category

    def main_category(self):
        return self.category.main_category.name_en


    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])