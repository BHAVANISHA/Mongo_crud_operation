# Generated by Django 4.1.13 on 2023-11-14 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mongo_crud_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
