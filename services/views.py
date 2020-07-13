from django.shortcuts import render
from services.models import *
from services.forms import *


# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def service_view(request):
    income_tax_activate= request.POST.get('check_01')
    companies_activate= request.POST.get('check_02')
    gst_tax_activate= request.POST.get('check_03')
    accounting_activate= request.POST.get('check_04')
    print(accounting_activate,companies_activate,gst_tax_activate,income_tax_activate)
    if request.method == 'GET':
        return render(request, 'service.html')
    
    class_of_income_tax = str(income_tax_activate)
    class_of_gst_tax=str(gst_tax_activate)
    class_of_companies=str(companies_activate)
    class_of_accounting=str(accounting_activate)
    print("=="*50)
    print("**"*50)
    
    if(class_of_income_tax=='None'):
        income_tax_activate=0
    if(class_of_gst_tax=='None'):
        gst_tax_activate=0
    if(class_of_companies=='None'):
        companies_activate=0
    if(class_of_accounting=='None'):
        accounting_activate=0
        
    activate_info_object= ActiveServicesModel( income_tax_activate=income_tax_activate,gst_tax_activate=gst_tax_activate,
    companies_activate=companies_activate,accounting_activate=accounting_activate)

    activate_info_object.save()
    return render(request, 'service.html')

def incometax_view(request):
    # print(request.POST)
    # print(request.method)
    # print(request.POST.get('first_install'))
    # print('incometax_view')

    first_install= request.POST.get('first_install')
    second_install= request.POST.get('second_install')
    third_install= request.POST.get('third_install')
    fourth_install= request.POST.get('fourth_install')
    taxreturn= request.POST.get('taxreturn')
    tdsreturn = request.POST.get('tdsreturn')
    if request.method == 'GET':
        return render(request, 'incometax.html')
    
    incom_obj = IncomeTaxModel(first_install_due=first_install, second_install_due =second_install,
    third_install_due=third_install, fourth_install_due=fourth_install,
    tax_return_date= taxreturn,tds_return_date=tdsreturn)

    incom_obj.save()

    # print('Saved')
    return render(request,'activation_sent.html')


def gst_view(request):
    # print(request.POST)
    # print(request.method)
    # print(request.POST.get('first_install'))
    # print('incometax_view')

    # Duration= request.POST.get('Duration')
    # first_due_GSTR1= request.POST.get('first_due_GSTR1')
    # first_due_GSTR3B= request.POST.get('first_due_GSTR3B')
    # annual_return_GSTR3B= request.POST.get('annual_return_GSTR3B')
    # if request.method == 'GET':
    #     return render(request, 'gst.html')
    

    # incom_obj = GstModel(Duration=Duration,first_due_1=first_due_GSTR1, 
    #             first_due_3b=first_due_GSTR3B, annual_due_3b= annual_return_GSTR3B)

    # incom_obj.save()

    # print('Saved')
    return render(request,'activation_sent.html')
 

def companies_act_view(request):
    # print(request.POST)
    # print(request.method)
    # print(request.POST.get('Return_1'))
    # print('companies_act_view')

    Return_1= request.POST.get('Return_1')
    Return_2= request.POST.get('Return_2')

    if request.method == 'GET':
        return render(request, 'companies_act.html')
    
    incom_obj = CompaniesActModel(first_return_due=Return_1, second_return_due =Return_2)

    incom_obj.save()

    # print('Saved')
    return render(request,'activation_sent.html')


def accounting_view(request):
    # print(request.POST)
    # print(request.method)
    # print(request.POST.get('Return_1'))
    # print('companies_act_view')

    Return_1= request.POST.get('Return_1')
    Return_2= request.POST.get('Return_2')

    if request.method == 'GET':
        return render(request, 'accounting.html')
    
    incom_obj = AccountingModel(first_return_due=Return_1, second_return_due =Return_2)

    incom_obj.save()

    # print('Saved')
    return render(request,'activation_sent.html')


