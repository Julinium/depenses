from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from depenses import settings



class xCategory(models.Model):
    class Meta:
        verbose_name = _("expense category")
        verbose_name_plural = _("expense categories")

    name = models.CharField(_("Name"), max_length=20)
    order = models.IntegerField(_("Order"), default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    # icon = 

    def __str__(self):
        return self.name



class nCategory(models.Model):
    class Meta:
        verbose_name = _("income category")
        verbose_name_plural = _("income categories")

    name = models.CharField(_("Name"), max_length=20)
    order = models.IntegerField(_("Order"), default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    # icon = 

    def __str__(self):
        return self.name



class Account(models.Model):
    class Meta():
        verbose_name = _("account")
        verbose_name_plural = _("accounts")

    name = models.CharField(_("Name"), max_length=20)
    reference = models.CharField(_("Reference"), max_length=64)
    order = models.IntegerField(_("Order"), default=1)
    balance = models.DecimalField(_("Balance"), max_digits=10, decimal_places=2, default=0)
    balance_date = models.DateTimeField(_("Balance Date"), default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " (" + str(self.user) + ")"


class AccountBalance(models.Model):
    account = models.ForeignKey(Account, verbose_name=_("Account"), on_delete=models.CASCADE)
    balance = models.DecimalField(_("Balance"), max_digits=10, decimal_places=2, default=0)
    balance_date = models.DateTimeField(_("Balance Date"), default=timezone.now)


class Expense(models.Model):
    class Meta:
        verbose_name = _("expense")
        verbose_name_plural = _("expenses")
        ordering = ['-date', '-amount', '-date_modified']
        
    date = models.DateField(_("Date"), default=timezone.now)
    vendor = models.CharField(_("Vendor"), max_length=40)
    category = models.ForeignKey(xCategory, verbose_name=_("Category"), on_delete=models.PROTECT)
    account = models.ForeignKey(Account, verbose_name=_("Account"), on_delete=models.PROTECT)
    amount = models.DecimalField(_("Amount"), max_digits=10, decimal_places=2)
    description = models.CharField(_("Description"), max_length=80, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.category.name) + ': ' + str(self.amount)



class Income(models.Model):
    class Meta:
        verbose_name = _("income")
        verbose_name_plural = _("incomes")
        ordering = ['-date', '-amount', '-date_modified']
        
    date = models.DateField(_("Date"), default=timezone.now)
    # source = models.CharField(_("Source"), max_length=40)
    category = models.ForeignKey(nCategory, verbose_name=_("Category"), on_delete=models.PROTECT)
    account = models.ForeignKey(Account, verbose_name=_("Account"), on_delete=models.PROTECT)
    amount = models.DecimalField(_("Amount"), max_digits=10, decimal_places=2)
    description = models.CharField(_("Description"), max_length=80, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)



class Transfer(models.Model):
    class Meta:
        verbose_name = _("transfer")
        verbose_name_plural = _("transfers")
        ordering = ['-date', '-amount', '-date_modified']
        
    date = models.DateField(_("Date"), default=timezone.now)
    # source = models.CharField(_("Source"), max_length=40)
    fm = models.ForeignKey(Account, verbose_name=_("From"), related_name = _("Source"), on_delete=models.PROTECT)
    to = models.ForeignKey(Account, verbose_name=_("To"), related_name = _("Destin"), on_delete=models.PROTECT)
    amount = models.DecimalField(_("Amount"), max_digits=10, decimal_places=2)
    description = models.CharField(_("Description"), max_length=80, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
############## BETTER THAN SIGNALS ######################################
# When saving an expense, edit the related account accordingly, in place.
# For safety, remove Expenses managements from the Admin site.
#########################################################################

# @receiver(post_save, sender=Expense)
# def xp_add(sender, created, instance, **kwargs):
#     xp = instance
#     ac = instance.account
#     if created:
#         ac.balance -= instance.amount
#     else:
#         # TODO: Send a signal before editing an Expense, 
#         # so We can know what was the amount before editing.
#         #############################
#         ##### vvvvv WRONG vvvvv #####
#         #############################
#         ac.balance -= instance.amount
#     ac.balance_date = timezone.now()
#     ac.save()
#     return ac
    
# @receiver(post_delete, sender=Expense)
# def xp_del(sender, instance, **kwargs):
#     xp = instance
#     ac = xp.account
#     ac.balance += xp.amount
#     ac.balance_date = timezone.now()
#     ac.save()
#     return ac
    
    