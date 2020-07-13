from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms
import psycopg2
# Create your views here.
conn = psycopg2.connect(database="Reminder", user = "postgres", password = "jigarpinakin", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
def home_view(request):
    print('home_view')
    return render(request, 'home.html')


def profile_view(request, username):
    return render(request, 'service.html')


def login_view(request):
    if request.method=='GET':
        return render(request, 'login.html')
    print(request)
    print(request.POST)

    email_user_input= request.POST.get('email')
    pass_user_input = request.POST.get('password')
    email_database_input=""
    pass_database_input=""
    print(email_user_input)
    print(pass_user_input)
    print("=="*50)
    query= "SELECT * FROM public.internalapp_profile WHERE internalapp_profile.email = '"+ str(email_user_input) +"'"
    print(query)
    cur.execute(query)
    rows = cur.fetchall()
    print(rows)
    print(type(rows))
    for row in rows:
        email_database_input = row[3]
        pass_database_input= row[9]
    print(email_database_input)
    print(email_user_input)
    print(pass_database_input)
    print(pass_user_input)
    print("**"*50)
    print("**"*50)
    print("**"*50)
    if(email_database_input==email_user_input):
        print("User emails are matching")
        if(pass_database_input==pass_user_input):
            print("Password matched too")
            print("Congratulations and celebrations for login")
            query2= "SELECT username FROM public.internalapp_profile WHERE internalapp_profile.email = '"+ str(email_user_input) +"'"
            cur.execute(query2)
            rows1= cur.fetchall()
            print(rows1)
            print(type(rows1))
            for row in rows1:
                username_database_input = row[0]
            args={}
            args['username_data']= username_database_input
            
            print(username_database_input)
            return render(request, 'login_confirmation.html',args)
            # return render(request, 'profile.html',args)
        
        else:
            print("Password is incorrect")
            return HttpResponse('Password is incorrect')
    
    else:
        print("Email adress does not found please login")
        return HttpResponse('Email adress does not found please login')






    # conn = psycopg2.connect(database="Reminder", user = "postgres", password = "jigarpinakin", host = "127.0.0.1", port = "5432")
    # print(conn)
    # print("database is connected")
    # cur = conn.cursor()
    # cur.execute(""" SELECT * FROM public.internalapp_profile WHERE internalapp_profile.first_name = 'Ansh' """)
    # rows = cur.fetchall()
    # print(rows)
    # print("Table created successfully")
    # print('login_view')
    if request.method=='GET':
        return render(request, 'login.html')

def signup_view(request):
    print(request.POST)
    print(request.method)
    print(request.POST.get('firstname'))
    print('signup_view')
    if request.method=='GET':
        return render(request, 'signup.html')
    
    else:
        if True:

            # form = forms.SignUpForm(request.POST)
            # form.save()

            firstname= request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            username=request.POST.get('username')
            phone=request.POST.get('phone')
            email=request.POST.get('email')
            gst=request.POST.get('gst')
            aadhar=request.POST.get('aadhar')
            pan=request.POST.get('pan')
            passer=request.POST.get('password')
            repass=request.POST.get('repass')  

            sign_obj =models.Profile(first_name=firstname,last_name=lastname,email=email,username=username,
            phone_no=phone,gst=gst,aadhar=aadhar,pan=pan,password1=passer,password2=repass)  

            sign_obj.save()
            print('Saved')
            return HttpResponse('jigar_checks_database')

def activation_sent_view(request):
    print('activation_sent_view')
    return render(request, 'activation_sent.html')

def jigar_checks_database(request):
    print('jigar_checks_database')
    return HttpResponse('jigar_checks_database')
