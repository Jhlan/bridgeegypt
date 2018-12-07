from django.shortcuts import render
from products.models import Product, ProductMainCategory, ProductSubCategory
from django.utils.translation import ugettext_lazy as _
from main.models import Page,Message



from .forms import ContactForm

# Create your views here.

def index(requst):
    data=Product.objects.all()

    return render(requst,'main/index.html',context={'data':data,})

def contact(request):

    data=Page.objects.filter(id=1)
    count=data[0].click_count

    count+=1

    Page.objects.filter(id=1).update(click_count=count)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            success_alert=_('Thanks, Your message sent.')
            return render(request,'main/contact.html',context={'data':data,'form':form,'success_alert':success_alert})
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'data':data,'form': form})


    #main_category=ProductMainCategory.objects.all()
    #'main_category':main_category

    #

def about(requst):

    data_inner=Page.objects.filter(id=2)
    count=data_inner[0].click_count

    count+=1

    Page.objects.filter(id=2).update(click_count=count)


    #main_category=ProductMainCategory.objects.all()
    #'main_category':main_category

    return render(requst,'main/inner-page.html',context={'data_inner':data_inner,})




# def home(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             pass  # does nothing, just trigger the validation
#     else:
#         form = ContactForm()
#     return render(request, 'main/contact.html', {'form': form})


# def message_send(request):
#     #Message.objects.create(name=request['form-name'])

#     return render(request,'main/index.html')