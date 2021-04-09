from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.del_task, name='delete'),

]
