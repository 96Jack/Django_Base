from pickle import PERSID
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from ModelFilter.models import Person



# Create your views here.

# 筛选出满足条件的数据
def t_filter(request):
    persons = Person.objects.filter(age__gt=25)
    for person in persons:
        print(person.name)
    return HttpResponse('条件查询成功')

def t_in(request):
    persons = Person.objects.filter(age__in=(16, 23))
    for person in persons:
        print(person.name)
    return HttpResponse('条件查询成功')


# 筛选出不满足条件的数据
def t_exclude(request):
    persons = Person.objects.exclude(age__gt=25)
    for person in persons:
        print(person.name)
    return HttpResponse('条件查询成功')

# 链式调用： 多个filter和exclude联合调用
def t_fil_ex(request):
    names = []
    persons = Person.objects.filter(age__gt=16).exclude(age=28)
    for person in persons:
        print(names.append(person.name))
    data = {
        'code':200,
        'name': names
    }
    # return HttpResponse('链式条件查询成功')
    return JsonResponse(data=data, json_dumps_params={'ensure_ascii':False})

# 创建对象的四种方式
def create_obj(request):
    # 创建对象1
    # p = Person()
    # p.name = 'ww'
    # p.age = '12'
    # p.save()

    # 创建对象2
    # p = Person(name='qq', age='23')
    # p.save()

    # 创建对象3
    # p = Person.objects.create(name='tq', age='3')
    # p.save()

    # 创建对象4: 通过类方法创建对象
    p = Person.create(name='ls', age='14')
    p.save()
    return HttpResponse('创建成功')

def QSet(request):
    # persons = Person.objects.order_by('-id')
    # 倒叙
    persons = Person.objects.order_by('-age')
    # <class 'django.db.models.query.QuerySet'>
    print(type(persons.values()))
    for person in persons.values():
        print(person)
    return HttpResponse('QuerySet 查询集')

def getOne(request):

    # 返回模型对象 <class 'ModelFilter.models.Person'>
    # person = Person.objects.get(pk=2)
    # print(type(person))
    # print(person.name)

    # 返回模型对象
    # p = Person.objects.all().first()
    # p = Person.objects.all().last()
    # print(type(p))
    # print(p.name)   
     
    # 返回int 类型 ： <class 'int'> 
    # p = Person.objects.all().count()
    # print(type(p))
    # print(p)
    # if p > 0:
    #     print('count应用场景, 判断是否获取到数据')

    # 返回布尔值
    p =Person.objects.filter(name='ls')
    # p = Person.objects.all()
    print(type(p.exists()))
    if p.exists():
        print('True')
    else:
        print('False')
    return HttpResponse('查询成功')