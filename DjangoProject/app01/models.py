from django.db import models

# Create your models here.
# 创建表，位于app01目录下，表名为类名
# 类创建好以后要在项目目录下(DjangoProject)进行终端的运行:（1）python manage.py makemigrations（2）python manage.py migrate
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
class changed(models.Model):
    area = models.CharField(max_length=32)
    hobby = models.CharField(max_length=64)
    num = models.IntegerField()
    ## 若是在已有表的基础上增加属性列的话，需要设置默认值，
    ## 若是在已有表的基础上删除属性列的话，只需要加上注释或删除，
    count = models.IntegerField(default=0)
    ## sport = models.CharField(max_length=64)