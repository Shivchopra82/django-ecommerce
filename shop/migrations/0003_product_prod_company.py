# Generated by Django 3.2.2 on 2021-05-11 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210510_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_company',
            field=models.CharField(default='made in chinas', max_length=50),
        ),
    ]