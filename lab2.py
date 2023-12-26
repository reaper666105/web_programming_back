from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route("/lab2/")
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/example')
def example():
    
    name, group, course, lab_num= 'Юшков Вадим', 'ФБИ-11', '3 курс', 2
    fruits = [
      {'name':'яблоки', 'price':100},
      {'name':'груши', 'price':120},
      {'name':'апельсины', 'price':80},
      {'name':'мандарины', 'price':95},
      {'name':'манго', 'price':321},
    ]
    return render_template('example.html', name=name, course=course, group=group, lab_num=lab_num, fruits=fruits)


@lab2.route('/lab2/flowers')
def show_flowers():
    flowers_data = [
        {'image': 'flow_1.jpg', 'description': 'Beautiful red rose'},
        {'image': 'flow_2.jpg', 'description': 'Colorful tulips in the garden'},
        {'image': 'flow_3.jpg', 'description': 'Elegant white lily'},
        {'image': 'flow_4.jpg', 'description': 'Vibrant yellow sunflower'},
        {'image': 'flow_5.jpg', 'description': 'Exotic orchid in full bloom'}
    ]
    return render_template('flowers.html', flowers=flowers_data)


@lab2.route('/lab2/flow/')
def flow():
    return render_template('flow.html')
