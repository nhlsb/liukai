# Generated by Django 4.0 on 2022-10-03 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_alter_userinfo_gender'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]