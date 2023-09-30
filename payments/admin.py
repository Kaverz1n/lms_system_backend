from django.contrib import admin

from payments.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'date', 'amount', 'method',)
    list_filter = ('date', 'method',)
    search_fields = ('user', 'course', 'lesson',)
    ordering = ('-date',)
