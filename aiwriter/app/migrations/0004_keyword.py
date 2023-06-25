# Generated by Django 4.2.2 on 2023-06-22 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_wesitemodel_delete_wesite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('article', models.TextField(blank=True)),
            ],
        ),
    ]