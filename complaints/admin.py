from django.contrib import admin
from .models import Complaint, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'priority', 'status')
    list_filter = ('category', 'priority', 'status')
    search_fields = ('name', 'message', 'admin_response')
    fields = (
        'name',
        'message',
        'category',
        'priority',
        'status',
        'admin_response',
    )