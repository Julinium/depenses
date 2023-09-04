from django.contrib import admin

from base.models import Account, nCategory, xCategory, Expense, Income, Transfer

admin.site.register(Account)
admin.site.register(nCategory)
admin.site.register(xCategory)
# admin.site.register(Expense)
# admin.site.register(Income)
# admin.site.register(Transfer)