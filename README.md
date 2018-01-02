Flask 两个主要依赖：
```
路由、调试和Web 服务器网关接口子系统由Werkzeug提供；
模板系统由Jinja2提供
```
自由使用第三方插件补齐高频操作
```
数据库访问
Web 表单验证和用户认证等高级功能
```

```
source venv/bin/activate
source venv/bin/deactivate
```

一个简单的程序

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
        return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
        return '<h1>Hello,%s!</h1>' % name

if __name__ == '__main__':
        app.run(host='0.0.0.0',debug=True)

```
```
current_app 程序上下文 当前激活程序的程序实例

g 程序上下文 处理请求时用作临时存储的对象。每次请求都会重设这个变量

request 请求上下文 请求对象，封装了客户端发出的HTTP 请求中的内容

session 请求上下文 用户会话，用于存储请求之间需要“记住”的值的词典
```


Flask 使用app.route 修饰器或者非修饰器形式的app.add_url_rule() 生成映射
```
>>> from hello import app
>>> app.url_map
Map([<Rule '/' (HEAD, OPTIONS, GET) -> index>,
<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
<Rule '/user/<name>' (HEAD, OPTIONS, GET) -> user>])
```

程序上下文
```
from hello import app
from flask import current_app
app_ctx = app.app_context()
app_ctx.push()
print current_app.name
app_ctx.pop()
```

请求上下文
```
from flask import request
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
        user_agent = request.headers.get('User-Agent')
        return '<p>Your browser is %s</p>' % user_agent

if __name__ == '__main__':
        app.run(host='0.0.0.0',debug=True)
```

钩子函数

```
• before_first_request：
注册一个函数，在处理第一个请求之前运行。
• before_request：
注册一个函数，在每次请求之前运行。
• after_request：
注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行。
• teardown_request：
注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行。
```
```txt
在请求钩子函数和视图函数之间共享数据一般使用上下文全局变量g。例如，before_
request 处理程序可以从数据库中加载已登录用户，并将其保存到g.user 中。随后调用视
图函数时，视图函数再使用g.user 获取用户。
```

扩展脚本
```
pip install flask-script
```

```
from flask.ext.script import Manager
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
```

```
python hello.py runserver -h 0.0.0.0 -p

optional arguments:
  -?, --help            show this help message and exit
  -h HOST, --host HOST
  -p PORT, --port PORT
  --threaded
  --processes PROCESSES
  --passthrough-errors
  -d, --debug           enable the Werkzeug debugger (DO NOT use in production
                        code)
  -D, --no-debug        disable the Werkzeug debugger
  -r, --reload          monitor Python files for changes (not 100% safe for
                        production use)
  -R, --no-reload       do not monitor Python files for changes
  --ssl-crt SSL_CRT     Path to ssl certificate
  --ssl-key SSL_KEY     Path to ssl key

```

```
状态码

@app.route('/')
def index():
    return '<h1>Bad Request</h1>', 400

make_response()
set_cookie()

from flask import make_response
@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

redirect()
  
from flask import redirect
@app.route('/')
def index():
    return redirect('http://www.example.com')

abort

from flask import abort
@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name
```
