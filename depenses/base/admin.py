from django.contrib import admin

from base.models import Account, nCategory, xCategory, Expense, Income, Transfer, AccountBalance


class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'user', 'reference', 'description']
    search_fields = ['name', 'reference', 'description']
    list_filter = ['user']
    ordering = ('order', 'user', 'name')


admin.site.register(Account, AccountAdmin)
admin.site.register(AccountBalance)
admin.site.register(nCategory)
admin.site.register(xCategory)
# admin.site.register(Expense)
# admin.site.register(Income)
# admin.site.register(Transfer)