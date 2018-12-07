from django.urls import path
from django.views.generic import RedirectView
from . import views
urlpatterns=[
    path('',RedirectView.as_view(url='/main/',permanent=True)),
    path('subcategory/<int:id>',views.SubcategoryListView.as_view(),name='productsubcategory_list'),
    # path('anchors/',views.anchors,name='anchors'),
    # path('gas/',views.gas,name='gas'),
    # path('others/',views.others,name='others'),

    path('subcategory/products-list/<int:id>',views.ProductsListView.as_view(),name='product_list'),
    path('subcategory/products-list/product-detail/<int:pk>',views.ProductsDetailView.as_view(),name='product_detail'),

    path('results/',views.search,name='search')

]