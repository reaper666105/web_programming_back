from flask import Blueprint, redirect, url_for


lab1 = Blueprint('lab1', __name__)


@lab1.route('/')
@lab1.route('/index')
def start():
    return redirect("/menu", code=302)


@lab1.route('/menu')
def menu():
    return  """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>НГТУ, ФБ, Лабораторные работы</title> 
    </head>
    <body>
        <header> 
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        
        <div>Смотрите ниже</div>
        <main><a href="/lab1">Лабораторная работа №1</a></main>
        <main><a href="/lab2">Лабораторная работа №2</a></main>
        <main><a href="/lab3/form1">Лабораторная работа №3</a></main>

        <footer> &copy; Vadim Yushkov, FBI-11, 3rd year, 2023</footer>
    </body>
</html>
"""


@lab1.route('/lab1')
def lab():
    return """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Юшков. Лабораторная 1</title> 
    </head>
    <body>
        <header> 
            НГТУ, ФБИ, Лабораторная работа 1
        </header>
        
        <h1>Web-server with Flask</h1>

        <h2>Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов

            веб-приложений, сознательно предоставляющих лишь самые ба-
            зовые возможности.
        </h2>
        <a href="/menu">Menu</a>
        <h2>Реализованные роуты</h2>
        <div><a href="/lab1/oak">ДУБ</a></div>
        <div><a href="/lab1/student">СТУ ДЕНТ</a></div>
        <div><a href="/lab1/python">Python</a></div>

        <footer> &copy; Vadim Yushkov, FBI-11, 3rd year, 2023</footer>
    </body>
</html>
"""


@lab1.route('/lab1/oak')
def oak():
    return '''
<!DOCTYPE html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''" width=500px, height=400px>
    </body>
</html>
'''


@lab1.route("/lab1/student")
def student():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Юшков В.Д. лабораторная 1</title>
</head>
<body>
<header>
НГТУ ФБИ Лабораторная работа 1
</header>
    
<h1>Юшков В.Д.</h1>

<img src="''' + url_for('static', filename='NSTU.jpg') + '''"  width=800px, height=500px>


<footer>
@copy; Юшков В.Д. ФБИ-11 3курс,2023
</footer>

</body>
</html>
'''


@lab1.route("/lab1/python")
def python():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Юшков В.Д. лабораторная 1</title>
</head>
<body>
   <header>НГТУ ФБИ Лабораторная 1</header> 

   <h1>python</h1>

   <h2>Python — интерпретируемый язык программирования общего
    назначения. Создан Хрисом Гоффом в начале 1990-х годов, представлен в 1991 году.'</h2>

    <img src="''' + url_for('static', filename='Python.png') + '''" width=800px, height=400px>

    <footer>
    @copy; Юшков В.Д. ФБИ-11 3курс,2023
    </footer>

</body>
</html>
'''