from django.urls import path
from main import views
urlpatterns=[
    path('',views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    #path('send-message/',views.message_send,name='send_message')
]