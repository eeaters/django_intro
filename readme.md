# 项目描述
学习python语言时,看下python的django框架构建web项目的手感

- 参照: [三小时带你入门Django框架](https://www.bilibili.com/video/BV1Sf4y1v77f) 

# 项目简介
- 默认的SQLite进行数据存储
- 使用template模板引擎
- 使用bootstrap实现静态页面编写

# 项目启动
- python manage.py runserver  
- 页面: http://localhost:8000/blog/index
- admin: http://localhost:8000/admin (用户名和密码需要通过命令创建)

# 命令

| 功能      | 命令                                  |
|---------|-------------------------------------|
| 创建项目    | django-admin startproject {project} |
| 运行项目    | python manage.py runserver          |
| 创建应用    | python manage.py startapp {app}     |
| 模型迁移    | python .\manage.py makemigrations   |
|         | python .\manage.py migrate          |
| shell   | python manage.py shell              |
| 管理员用户创建 |  python .\manage.py createsuperuser |


