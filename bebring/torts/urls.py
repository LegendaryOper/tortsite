from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('tort/<int:pk>/', GetTortPage.as_view(), name='get_tort_page'),
    path('category/<int:category_pk>/', GetCategory.as_view(), name='category_page'),
    path('make_offer/', OfferFormView.as_view(), name='make_offer'),
    path('send_problem/', ProblemFormView.as_view(), name='send_problem'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
]
