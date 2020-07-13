"""databasechecker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_view, name="service"),
    path('incometax/', views.incometax_view, name="incometax"),
    path('gst/', views.gst_view, name="gst"),
    path('companies_act/', views.companies_act_view, name="companies_act"),
    path('accounting/', views.accounting_view, name="accounting"),
]

##########################################################################
# migrations.CreateModel(
#             name='Profile',
#             fields=[
#                 ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
#                 ('first_name', models.CharField(blank=True, max_length=100)),
#                 ('last_name', models.CharField(blank=True, max_length=100)),
#                 ('email', models.EmailField(max_length=150)),
#                 ('username', models.CharField(blank=True, max_length=100)),
#                 ('phone_no', models.IntegerField(blank=True)),
#                 ('gst', models.IntegerField(blank=True)),
#                 ('aadhar', models.IntegerField(blank=True)),
#                 ('pan', models.IntegerField(blank=True)),
#                 ('password1', models.CharField(max_length=100)),
#                 ('password2', models.CharField(max_length=100)),
#                 ('signup_confirmation', models.BooleanField(default=False)),
#                 ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
#             ],
#         ),