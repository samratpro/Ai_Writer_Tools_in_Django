# Generated by Django 4.2.2 on 2023-06-19 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_wesite_website_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='WesiteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_name', models.CharField(max_length=150)),
                ('website_url', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=100)),
                ('app_pass', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Wesite',
        ),
    ]
