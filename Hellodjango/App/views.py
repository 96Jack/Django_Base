
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

from App.models import Grade, Student, User

# Create your views here.

def index_app(request):
    return HttpResponse(" this is a App index")


# 返回html页面，基于应用App
def app_html(request):
    return render(request, template_name='score.html')    
# 返回html页面， 基于项目
def pro_html(request):
    return render(request, template_name='base.html')    


# 模板语法的两种方式
def one(request):
    context = {
        'name' :'zs',
        'age' : '18',
        "score_list" : [100, 90, 80, 70]
    }

    return render(request, template_name='test_temp.html', context=context)

def two(request):
    # 加载
    html_obj = loader.get_template('base.html')
    context = {
        'name':'ls',
    }
    # 渲染
    context_obj = html_obj.render(context=context)
    return HttpResponse(context_obj)


def three(request):
    return HttpResponse("three")


# DML: models中数据的增删改查
def add_User(request):

    user = User()
    user.name = 'qwe'
    user.age = '12'
    user.save()

    return HttpResponse('添加成功')

def findByid(request):
    user = User.objects.get(pk=1)
    print(user.name, user.age)
    return HttpResponse("查询成功")

def findAll(request):
    users = User.objects.all()
    for user in users:
        print(user.name, user.age)
    return HttpResponse('查询成功')

def update(request):
    # 更改和删除基于查询，且更改完需要保存
    user = User.objects.get(pk=1)
    user.name = 'asd'
    user.save()
    return HttpResponse('修改成功')

def delete(request):
    # 删除之后不需要保存 
    user = User.objects.get(pk=2)
    user.delete()
    return HttpResponse('删除成功')    


# Base_1练习
def get_grade(request):
    grades = Grade.objects.all()
    context = {
        'grades':grades
    }
    return render(request, 'grade.html', context=context)

# 查询对应班级的学生
def get_student(request):
    # 接收请求参数: GET : 全部大写
    id = request.GET.get('id')
    students = Student.objects.filter(s_grade_id=id)
    context = {
        'students': students
    }
    return render(request, 'student.html', context=context)

