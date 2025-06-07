from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.get_all_items),
    path('item/', views.get_single_item),
    path('items/new/', views.create_item),
]
