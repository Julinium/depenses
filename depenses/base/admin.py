from django.contrib import admin

from . models import nCategory, xCategory, Expense, Income, Transfer

admin.site.register(nCategory)
admin.site.register(xCategory)

# admin.site.register(Expense)
# admin.site.register(Income)
# admin.site.register(Transfer)