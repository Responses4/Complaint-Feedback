from django.urls import path
from . import views

app_name = 'complaints'

urlpatterns = [
    path('', views.complaint_form, name='complaint_form'),
    path('success/', views.success, name='success'),
    path('list/', views.complaint_list, name='complaint_list'),
    path('detail/<int:pk>/', views.complaint_detail, name='complaint_detail'),
    path('api/', views.complaint_api, name='complaint_api'),
    path('api/<int:pk>/', views.complaint_detail_api, name='complaint_detail_api'),
    path('reply/<int:complaint_id>/', views.reply_to_complaint, name='reply'),
]
