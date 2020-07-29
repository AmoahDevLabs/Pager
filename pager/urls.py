from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.index, {'page_name': ''}, name='home'),
    path('<str:page_name>', views.index, name='index'),
]
