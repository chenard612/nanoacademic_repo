from django.urls import path
from . import views

app_name = 'elements'

urlpatterns =[
     path('', views.elements, name="elements"),
     path('details/<str:symbol>/', views.element_detail, name="element_detail"),
     ]
