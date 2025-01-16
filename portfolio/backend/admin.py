from django.contrib import admin
from .models import PortfolioProject

@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')  # Columns displayed in the admin list view
    search_fields = ('title', 'category')              # Enable search by title and category
    list_filter = ('category', 'created_at')           # Add filters for category and creation date
    ordering = ('-created_at',)                        # Order projects by creation date (newest first)

    # Customize the form in the admin
    fieldsets = (
        ("Basic Information", {
            'fields': ('title', 'description', 'category')
        }),
        ("Image", {
            'fields': ('image',),
        }),
        ("Additional Info", {
            'fields': ('created_at', 'updated_at'),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')  # Make timestamps read-only
