# Generated by Django 2.2 on 2020-07-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveServicesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_tax_activate', models.BooleanField()),
                ('gst_tax_activate', models.BooleanField()),
                ('companies_activate', models.BooleanField()),
                ('accounting_activate', models.BooleanField()),
            ],
        ),
    ]
