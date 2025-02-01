from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('business_name', 'review_text')
    readonly_fields = ('created_at', 'updated_at')