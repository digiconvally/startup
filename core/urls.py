from django.urls import path
from .views import (PostListViews,
                    PostCreateViews,
                    PostDetailViews,
                    PostUpdateViews,
                    PostDeleteViews
                    )
# from . import views

urlpatterns = [
    path('', PostListViews.as_view(), name='index'),
    path('create/', PostCreateViews.as_view(), name='create'),
    path('detail/<int:pk>/', PostDetailViews.as_view(), name='detail'),
    path('update/<int:pk>/', PostUpdateViews.as_view(), name='update'),
    path('delete/<int:pk>/', PostDeleteViews.as_view(), name='delete'),


    # path('', views.Home, name='index'),
    # path('detail/<int:pk>', views.detaillistViews, name='detail'),
    # path('create/', views.PostCreate, name='create'),
    # path('update/<int:pk>/', views.PostUpdate, name='update'),
    # path('delete/<int:pk>/', views.PostDelete, name='delete'),
]
