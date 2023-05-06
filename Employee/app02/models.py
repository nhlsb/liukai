from django.db import models

# Create your models here.
class Department(models.Model):
    '''部门表'''

    title = models.CharField(verbose_name='标题',max_length=32)

class UserInfo(models.Model):
    '''员工表'''

    name = models.CharField(verbose_name='姓名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='余额',max_digits=10,decimal_places=2,default=0)
    creata_time = models.DateTimeField(verbose_name='时间')
    ## 该表由于要关联部门表，故引入部门id，名为depart_id，以下写为depart是因为Django中会自动将depart转换为depart_id
    ## 此处对于depart有约束，to表示与哪张表关联，to_field表示与表中哪一列关联
    ## on_delete=models.CASCADE表示级联删除，即部门表中的某一列删除时，员工表中的对应行也相应删除
    depart = models.ForeignKey(verbose_name='部门id',to='Department',to_field='id',on_delete=models.CASCADE)
    ## on_delete=models.SET_NULL表示置空，即部门表中的某一列删除时，员工表中的对应行位置为空
    ## depart = models.ForeignKey(to='Department', to_field='id', null=True,blank=True,on_delete=models.SET_NULL)
    gender_choices = ((1,'男'),(2,'女'))
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices)

