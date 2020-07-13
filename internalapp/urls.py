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
    path('', views.home_view, name="home"),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup_view, name="signup"),
    path('sent/', views.activation_sent_view, name="activation_sent"),
    # path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    path('jigar/',views.jigar_checks_database,name="Databse checker")
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