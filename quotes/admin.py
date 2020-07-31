from django.contrib import admin
from .models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company',
                    'submitted', 'quote_date', 'quote_price')

    list_filter = ('submitted', 'quote_date')
    readonly_fields = ('submitted',)
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'description')
        }),
        ('Contact Information', {
            'classes': ('collapse',),
            'fields': ('position', 'company',
                       'address', 'phone_number', 'website')
        }),
        ('Job Information', {
            'classes': ('collapse',),
            'fields': ('site_status', 'priority',
                       'job_file', 'submitted')
        }),
        ('Quote Admin', {
            'classes': ('collapse',),
            'fields': ('quote_date', 'quote_price',
                       'username')
        }),
    )


admin.site.register(Quote, QuoteAdmin)
