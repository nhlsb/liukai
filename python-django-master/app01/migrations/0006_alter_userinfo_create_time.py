# Generated by Django 4.0 on 2022-10-03 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_alter_userinfo_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateTimeField(null=True, verbose_name='入职时间'),
        ),
    ]