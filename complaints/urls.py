from django.urls import path
from .views import complaint_form, complaint_list

urlpatterns = [
    path('', complaint_form, name='complaint_form'),
    path('list/', complaint_list, name='complaint_list'),
]
