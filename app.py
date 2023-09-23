from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def start():
    return """
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

        <footer> &copy; Vadim Yushkov, FBI-11, 3rd year, 2023</footer>
    </body>
</html>
"""

@app.route('/lab1')
def lab1():
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

        <footer> &copy; Vadim Yushkov, FBI-11, 3rd year, 2023</footer>
    </body>
</html>
"""

