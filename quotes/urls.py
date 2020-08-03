from django.urls import path
from . import views
from .views import QuoteList, QuoteDetail, RegisterUser


urlpatterns = [
    path('', views.quote_req, name='quote-request'),
    path('show', QuoteList.as_view(), name='show-quotes'),
    path('show/<int:pk>', QuoteDetail.as_view(), name='quote-detail'),
]
