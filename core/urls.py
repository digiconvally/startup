from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='index'),
    path('detail/<int:pk>', views.detaillistViews, name='detail'),
]
