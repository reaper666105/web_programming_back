from flask import Flask

app=Flask(__name__)

@app.route('/')
def start():
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

        <footer> &copy; Vadim Yushkov, FBI-11, 3rd year, 2023</footer>
    </body>
</html>
"""


