from  django.urls import path
from . import views
app_name='ecomapp'

urlpatterns = [

    path('',views.allproduct,name='allproduct'),
    path('<slug:c_slug>/',views.allproduct,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetail, name='prodcatdetail')

]
