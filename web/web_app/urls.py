from django.urls import path
from . import views 

urlpatterns = [
    path('function/',views.function_based_view, name='function_based_view'),
    path('class/', views.ClassBasedView.as_view(), name='class_based_view'),
]