from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from main.models import Message

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,label=_("Your name"),
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                #'placeholder': 'Write your name here'
            }
        )
    )

    email = forms.EmailField(
        max_length=254,label=_("Your email"),required=False,
        widget=forms.EmailInput(attrs={'class':"form-control",})
    )

    phone = forms.CharField(

        widget=forms.TextInput(attrs={'class':"form-control",}),
        label=_('Phone Number'),max_length=14,
        validators=[
            RegexValidator(
                regex='^(00|[+]|0)[0-9]+$',
                message=_('Enter a valid phone number.'),
                code='invalid_phone'
            ),
        ],
    )


    subject = forms.CharField(
        max_length=100,label=_("Your subject"),
        widget=forms.TextInput(attrs={'class':"form-control "}),
    )

    body = forms.CharField(
        max_length=2000,label=_("Your message"),
        widget=forms.Textarea(attrs={'class':"form-control md-textarea",'rows':"3"}),
        #help_text='Write here your message!'
    )

    class Meta:
        model=Message
        fields=('name','email','phone','subject','body')


    def clean(self):
            cleaned_data = super(ContactForm, self).clean()
            name = cleaned_data.get('name')
            email = cleaned_data.get('email')
            phone = cleaned_data.get('phone')
            subject = cleaned_data.get('subject')
            body = cleaned_data.get('body')
            if not name and not email and not phone and not subject and not body:
                raise forms.ValidationError(_('You have to write something!'))


# class ContactForm(forms.Form):
#     name = forms.CharField(
#         max_length=100,label=_('Your name'),help_text=_('Write here your message!')
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 #'placeholder': 'Write your name here'
#             }
#         )
#     )
#     email = forms.EmailField(
#         max_length=254,label=_('Your email'),
#         widget=forms.EmailInput(attrs={'class': 'form-control'})
#     )

#     phone=forms.CharField(label=_('Phone Number'),max_length=14,blank=True,
#         validators=[
#             RegexValidator(
#                 regex='^(00|[+]|0)[0-9]+$',
#                 message=_('Phone must be in correct form'),
#                 code='invalid_phone'
#             ),
#         ], widget=forms.NumberInput(attrs={'class': 'form-control'}))

#     subject=forms.CharField(label=_('Subject'),max_length=100,
#             widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',

#             }
#           )
#         )

#     message = forms.CharField(
#         max_length=2000,label=_('Your message'),
#         widget=forms.Textarea(attrs={'class': 'form-control'}),
#         help_text='Write here your message!'
#     )

#     created_at = forms.DateTimeField(label=_('Date of sending'),auto_now_add=True)




# class SendMssageForm(forms.Form):
#     name=forms.CharField(label=_('user name'),max_length=100)
#     email=forms.EmailField(label=_('user email'))
#     phone=forms.CharField(label=_('Phone Number'),max_length=14,blank=True,
#         validators=[
#             RegexValidator(
#                 regex='^(00|[+]|0)[0-9]+$',
#                 message=_('Phone must be in correct form'),
#                 code='invalid_phone'
#             ),
#         ])

#     created_at = forms.DateTimeField(label=_('Date of sending'),auto_now_add=True)
#     subject=forms.CharField(label=_('message subject'),max_length=100)
#     body=forms.CharField(label=_('message body'),widget=forms.Textarea, max_length=1000,blank=True)
