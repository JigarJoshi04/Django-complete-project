from django.db import models

# Create your models here.

class ActiveServicesModel(models.Model):
    income_tax_activate = models.BooleanField(null=False, blank=False)
    gst_tax_activate = models.BooleanField(null=False, blank=False)
    companies_activate = models.BooleanField(null=False, blank=False)
    accounting_activate = models.BooleanField(null=False, blank=False)


class IncomeTaxModel(models.Model):
    first_install_due=models.DateField()
    second_install_due=models.DateField()
    third_install_due=models.DateField()
    fourth_install_due=models.DateField()
    tax_return_date=models.DateField()
    tds_return_date=models.DateField()

# class GstModel(models.Model) :
#     MONTHLY='Monthly'
#     QUATERLY= 'Quaterly'
#     DURATION_CHOICES = [
#         (MONTHLY, 'Monthly'),
#         (QUATERLY, 'Quaterly'),
#     ]
#     Duration = models.CharField(
#         max_length=50,
#         choices=DURATION_CHOICES,
#         default=MONTHLY,
#     )
#     first_due_1=models.DateField()
#     first_due_3b=models.DateField()
#     annual_due_3b=models.DateField()


class CompaniesActModel(models.Model):
    first_return_due=models.DateField()
    second_return_due=models.DateField()

class AccountingModel(models.Model):
    first_return_due=models.DateField()
    second_return_due=models.DateField()