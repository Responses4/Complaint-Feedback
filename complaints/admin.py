from django.contrib import admin
from .models import Complaint, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'priority', 'status', 'created_at')
    list_filter = ('category', 'priority', 'status')
    search_fields = ('name', 'message', 'reply')
    fields = ('name', 'message', 'category', 'reply') 
