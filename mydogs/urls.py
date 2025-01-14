from django.urls import path
from mydogs.views import DogAPIView
from django.urls import path
from django.urls import include, path
from mydogs import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('', views.Test_api, name='home'),
    path('api/dogs/', views.DogList.as_view(), name='dogs_list'),
    path('api/dogs/<int:pk>/', views.DogDetail.as_view(),  name='dogs_detail'),
    path('api/breed/', views.DogList.as_view(), name='breeds_list'),
    path('api/breed/<int:pk>/', views.DogDetail.as_view(), name='breeds_detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)