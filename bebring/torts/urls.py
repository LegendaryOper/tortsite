from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('tort=<int:pk>/', GetTortPage.as_view(), name='get_tort_page')
]
