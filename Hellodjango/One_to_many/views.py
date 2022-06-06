
from django.http import HttpResponse
from django.shortcuts import render

from One_to_many.models import Dept, Emp

# Create your views here.
def one(request):
    return HttpResponse("One_to_many")

# 根据部门名称获取职员名
def get_dept(request):
    depts = Dept.objects.all()
    context = {
        'depts':depts,
    }
    return render(request, 'dept.html', context=context)

def get_emp(request):
    id = request.GET.get('id')
    emps = Emp.objects.filter(e_dept_id=id)
    context = {
        'emps': emps,
    }
    return render(request, 'emp.html', context=context)


# 需求
#1. 给定从表数据，查询主表数据 eg: 查询员工赵丽颖所在的部门
#2. 给定主表数据，查询从表数据 eg: 查询开发部门的员工姓名

# 命名习惯： 函数一般使用小驼峰、表的字段名一般使用下划线命名


# 1. 给定从表数据，查询主表数据 eg: 查询员工赵丽颖所在的部门
# 显性属性
def getDname(request):
    emp = Emp.objects.filter(name='赵丽颖')[0]
    print(emp.e_dept.name)
    context = {

    }
    # return render(request, '', context=context)
    return HttpResponse('查询成功')


def getEname(request):
    dept = Dept.objects.filter(name='开发部')[0]
    print(dir(dept))
    emps = dept.emp_set.all()
    for emp in emps:
        print(emp.name)
    # dept.emp_set.name

    context = {

    }
    # return render(request, '', context=context)
    return HttpResponse('查询成功')
