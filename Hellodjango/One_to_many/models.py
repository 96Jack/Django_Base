from django.db import models

# Create your models here.

# =============一对多=============
# 部门表 
class Dept(models.Model):
    name = models.CharField(max_length=32)

# 员工表
class Emp(models.Model):
    name = models.CharField(max_length=32)
    e_dept = models.ForeignKey(Dept, on_delete=models.CASCADE)

# 元信息
# 指定表名或者字段名称
class Bird(models.Model):
    name = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    class Meta:
        db_table = 'bird'
        
