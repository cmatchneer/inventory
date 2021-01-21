from django.urls import path
from .views import (
    product_form_view, 
    product_delete_view,
    product_list_view,
    product_update_view,
    
)

app_name = 'product'
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('form/', product_form_view, name='product-list'),
    path('<int:id>/update/', product_update_view, name='product-update'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
]