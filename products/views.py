from django.shortcuts import render
from products.models import Product, ProductSubCategory,ProductMainCategory
from django.views import generic
from django.db.models import Q

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def index(requst):

    main_category=ProductMainCategory.objects.all()
    return render(requst,'main/index.html',{'main_category':main_category})

# def building(requst):
#     data=ProductSubCategory.objects.all().filter(main_category__id=2)
#     return render(requst,'products/product_sub_category.html',context={'data':data})

# def anchors(requst):
#     data=ProductSubCategory.objects.all().filter(main_category__id=1)
#     return render(requst,'products/product_sub_category.html',context={'data':data})

# def gas(requst):
#     data=ProductSubCategory.objects.all().filter(main_category__id=3)
#     return render(requst,'products/product_sub_category.html',context={'data':data})

# def others(requst):
#     data=ProductSubCategory.objects.all().filter(main_category__id=4)
#     return render(requst,'products/product_sub_category.html',context={'data':data})


class SubcategoryListView(generic.ListView):
    model=ProductSubCategory

    def get_queryset(self):


       return ProductSubCategory.objects.all().filter(main_category__id=self.kwargs['id'])


class ProductsListView(generic.ListView):
    model=Product
    paginate_by = 1

    def get_queryset(self):
        q=ProductSubCategory.objects.filter(id=self.kwargs['id'])
        number_of_tiems=q[0].click_count+1

        ProductSubCategory.objects.filter(id=self.kwargs['id']).update(click_count=number_of_tiems)

        return Product.objects.filter(category_id=self.kwargs['id'])


class ProductsDetailView(generic.DetailView):
    model=Product

    def get_queryset(self):
        q=Product.objects.filter(id=self.kwargs['pk'])
        number_of_tiems=q[0].click_count+1

        Product.objects.filter(id=self.kwargs['pk']).update(click_count=number_of_tiems)
        return Product.objects.filter(id=self.kwargs['pk'])




def search(request):

    template='products/product_list.html'
    query=request.GET.get('q')

    if query:
        res=Product.objects.filter(

                Q(name_ar__icontains=query)
                | Q(name_en__icontains=query)

                # | Q(description_ar__icontains=query)
                # | Q(description_en__icontains=query)

                # | Q(detail_ar__icontains=query)
                # | Q(detail_en__icontains=query)

                | Q(category__name_ar__icontains=query)
                | Q(category__name_en__icontains=query)

                | Q(category__main_category__name_ar__icontains=query)
                | Q(category__main_category__name_en__icontains=query)

                | Q(keywords_ar__icontains=query)
                | Q(keywords_en__icontains=query)

            )
    else:
         res=Product.objects.all()

    paginator = Paginator(res, 6)
    #print(paginator)
    p_r=paginator.page_range
    page = request.GET.get('page')

    contacts = paginator.get_page(page)



    return render(request,template,{"object_list":contacts,"paginator":paginator,'page_obj':p_r,"search":"yes"})
