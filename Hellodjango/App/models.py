
from statistics import mode
from django.db import models

# Create your models here.

class User(models.Model):
    # flask 中id必须写，字符串类型必须指定长度，且长度为2的倍数
    # django中自动添加主键列(primary_key=True)，不用写id, 字符串类型必须指定长度
    name = models.CharField(max_length=32)
    age  = models.IntegerField()



class Grade(models.Model):
    name = models.CharField(max_length=32)

# 外键关联Grade表，Django2.0之后外键必须写上on_delete
class Student(models.Model):
    name = models.CharField(max_length=32)
    # 外键s_grade_id 关联 主表主键id列
    # show create table App_student;
    # > FOREIGN KEY (`s_grade_id`) REFERENCES `App_grade` (`id`) 
    s_grade = models.ForeignKey(Grade, on_delete=models.CASCADE)



