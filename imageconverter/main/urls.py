from django.urls import path
from . import views
from .views import ResizeApi

urlpatterns = [
    path('', views.index,),
    path('resize/', views.resize,),
    path('api/resize/', ResizeApi.as_view())
]
