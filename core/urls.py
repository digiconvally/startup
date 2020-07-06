from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='index'),
    path('detail/<int:pk>', views.detaillistViews, name='detail'),
    path('create/', views.PostCreate, name='create'),
    path('update/<int:pk>/', views.PostUpdate, name='update'),
    path('delete/<int:pk>/', views.PostDelete, name='delete'),
]
