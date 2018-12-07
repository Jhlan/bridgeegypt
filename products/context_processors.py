from products.models import ProductMainCategory, ProductSubCategory, Product

def public_main_category(request):

    main_category=ProductMainCategory.objects.all()
    sub_category=ProductSubCategory.objects.all()

    data=Product.objects.all()

    loop_times=range(1,5)

    return {'sub_category':sub_category,'main_category':main_category,'data_public':data,"loop_times":loop_times }