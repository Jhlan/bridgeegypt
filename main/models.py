from django.db import models
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import RegexValidator

# Create your models here.
class Page(models.Model):
    name_ar=models.CharField(_('page name in arabic'), max_length=100)
    name_en=models.CharField(_('page name in english'), max_length=100)

    description_ar=models.TextField(_('page description in arabic'), max_length=1000, blank=True)
    description_en=models.TextField(_('page description in english'), max_length=1000, blank=True)

    click_count=models.IntegerField(_('times of click'), default=0,null=True, blank=True)

    detail_ar=RichTextUploadingField(_('page details in arabic'),blank=True)
    detail_en=RichTextUploadingField(_('page details in english'),blank=True)

    address_ar=RichTextField(_('address in arabic'),config_name='basic_ckeditor',help_text=_('<span style="color:red; font-size:14px;">Note:- Address will appears in Contact Us page only </span>'), blank=True)
    address_en=RichTextField(_('address in english'),config_name='basic_ckeditor',help_text=_('<span style="color:red; font-size:14px;">Note:- Address will appears in Contact Us page only </span>'), blank=True)

    phones=RichTextField(_('phones'),config_name='basic_ckeditor',help_text=_('<span style="color:red; font-size:14px;">Note:- Phones will appears in Contact Us page only </span>'), blank=True)

    websites=RichTextField(_('emails and website'),config_name='basic_ckeditor',help_text=_('<span style="color:red; font-size:14px;">Note:- Emails and website will appears in Contact Us page only </span>'), blank=True)

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name=_('Page')
        verbose_name_plural=_('Pages')


class Message(models.Model):
    name=models.CharField(_('user name'),max_length=100)
    email=models.EmailField(_('user email'))
    phone=models.CharField(_('Phone Number'),max_length=14,blank=True,
        validators=[
            RegexValidator(
                regex='^(00|[+]|0)[0-9]+$',
                message=_('Phone must be in correct form'),
                code='invalid_phone'
            ),
        ])

    created_at = models.DateTimeField(_('Date of sending'),auto_now_add=True)
    subject=models.CharField(_('message subject'),max_length=100)
    body=models.TextField(_('message body'), max_length=1000,blank=True)

    class Meta:
        verbose_name=_('Message')
        verbose_name_plural=_('Messages')

    def __str__(self):
        return f'{self.subject} from {self.name}'