from django.urls import path
from .views import complaint_form, complaint_list, complaint_api, success, complaint_detail_api

urlpatterns = [
    path('', complaint_form, name='complaint_form'),
    path('list/', complaint_list, name='complaint_list'),
    path('api/', complaint_api, name='complaint_api'),
    path('api/<int:pk>/', complaint_detail_api, name='complaint_detail_api'), 
    path('success/', success, name='success'),
]
