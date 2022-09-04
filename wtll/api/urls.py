from django.urls import include, path
from .views import list_products, group_products

urlpatterns = [
    # api
    path('api/v1/products/', list_products, name='list_products'),
    path('api/v1/products/group/', group_products, name='group_products'),
]
