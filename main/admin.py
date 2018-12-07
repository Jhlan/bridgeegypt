from django.contrib import admin
from main.models import Page, Message
from django.utils.translation import ugettext_lazy as _
# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    model=Page

    readonly_fields=('click_count',)

    list_display=('name_en','name_ar','click_count')

    search_fields=('name_en','name_ar')

    def has_add_permission(self, request):
        return False

    actions = None

    fieldsets=(
        (
            None,{
                'fields':('name_ar','name_en','description_ar',
                'description_en','click_count','detail_ar','detail_en',)
                }
        ),
        (
            _('Data for Contact Us Page only'),
            {
                'fields':('address_ar','address_en','phones','websites')
            }
        )

    )

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    model=Message

    #readonly_fields=('name','email','subject','body')

    list_display=('name','phone','subject','created_at')

    search_fields=('name','email','subject')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request,obj=None):
        return False


