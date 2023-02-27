from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints, name='endpoints'),
    path('advocates/', views.advocate_list, name='advocate_list'),
    path('advocates/<str:username>', views.advocate_details, name='advocate_details'),
]
