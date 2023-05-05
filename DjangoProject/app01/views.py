from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
## 编写视图函数
def index(request):
    return HttpResponse("欢迎使用！")

def user_list(request):
    return HttpResponse("用户列表！")

def user_add(request):
    return HttpResponse("用户添加！")


def user_html_list(request):
    ## 去app01目录下templates(模板)中去找html文件
    return render(request,"user_html_list.html")

def user_html_add(request):
    ## 去app01目录下templates(模板)中去找html文件
    return render(request,"user_html_add.html")

def tpl(request):
    name = "liukai"  ## 字符串
    roles = ["管理员","学生","俊"]  ## 列表
    dicts = {"name":"tom","age":18,"role":"学生"}  ## 字典
    mix_list = [
        {"name": "jack", "age": 20, "role": "保安"},
        {"name": "Anny", "age": 21, "role": "医生"},
        {"name": "Bob", "age": 22, "role": "警察"}
    ]
    return render(request,'tpl.html',{"n1":name,"n2":roles,"n3":dicts,"n4":mix_list})  ## 以字典形式返回

def news(request):
    ## 应用爬虫方法爬取第三方数据并显示在自己的前端上
    import requests
    urls = "http://www.chinaunicom.com.cn/api/article/NewsByIndex/3/2023/04/news"
    Headers = {"User-Agent":'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36 Edg/112.0.1722.39'}
    res = requests.get(url=urls,headers=Headers)
    data_list = res.json()
    print(data_list)
    return render(request,'news.html',{"news_list":data_list})

def something(request):

    ## 获取用户请求方式,通常有GET和POST两种方式
    print(request.method)
    ## 在url上传递值,例如:?n1=123
    print(request.GET)
    print(request.POST)
    ## 响应1
    return HttpResponse("返回内容")
    ## 响应2
    ## return render(request,"xxx.html")
    ## 响应3:重定向
    ## return redirect("https://www.baidu.com")

def login(request):

    if request.method == "GET":
        return render(request, 'login.html')
    else:
        print(request.POST)
        username = request.POST.get("user")
        password = request.POST.get("pwd")
        ## print(username)
        ## print(password)
        if username == "root" and password == "123":
            ## return HttpResponse("POST请求，登录成功！")
            ## 设置输入成功后跳转到其他页面
            return redirect("https://www.baidu.com")
        else:
            ## return HttpResponse("POST请求，登录失败！")
            ## 设置输入错误后重新进入登录页面，again参数用于控制反馈信息，上述60行中未写入again，则默认为空，故第一次上登录页面时无反馈信息
            return render(request, 'login.html',{"again":"用户名或密码错误，登录失败！"})


def orm(request):
    from app01 import models
    models.UserInfo.objects.create(name="佩奇",password="123",age=10)
    models.UserInfo.objects.create(name="乔治",password="456",age=5)
    models.UserInfo.objects.create(name="萝莉",password="789",age=4)
    models.UserInfo.objects.create(name="海皮",password="654",age=3)
    models.UserInfo.objects.create(name="塔格",password="321",age=2)

    models.UserInfo.objects.filter(age=4).delete()

    data_liat = models.UserInfo.objects.all()
    ## data_list是一个对象列表
    for i in data_liat:
        print(i.name,i.password,i.age)

    models.UserInfo.objects.filter(name="海皮").update(password="000")

    return HttpResponse("(辅助验证)：表中增删查改数据成功!")


def user_management(request):

    from app01 import models
    data_liat = models.UserInfo.objects.all()
    ## data_list是一个对象列表
    ## print(data_liat)
    for i in data_liat:
        print(i.name, i.password, i.age)
    return render(request,'user_management.html',{"data_liat":data_liat})

def user_management_add(request):
    from app01 import models
    if request.method == "GET":
        return render(request, 'user_management_add.html')
    else:
        print(request.POST)
        username = request.POST.get("user")
        password = request.POST.get("pwd")
        age = request.POST.get("age")
        models.UserInfo.objects.create(name=username, password=password, age=age)
    return redirect("http://127.0.0.1:8000/user_management/")

def user_management_delete(request):
    from app01 import models
    nid = request.GET.get("nid")
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user_management/")