from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

def reverse_str(str):
    reversed_str = str[::-1]
    return reversed_str

posts = [
    {
        'author': {
            'username': 'test-user'
        },
        'title': 'Traveling alone for the first time',
        'content': 'Johor Bahru, Penang in Malaysia',
        'date_posted': datetime.strptime('2022-05-01', '%Y-%m-%d'),
        'img_title': "https://i.pinimg.com/564x/10/17/0e/10170eaa4265dac1955af5716a475d8e.jpg",
        'img_class_1': "https://i.pinimg.com/564x/10/17/0e/10170eaa4265dac1955af5716a475d8e.jpg",
        'img_class_2': "https://i.pinimg.com/564x/df/07/ae/df07ae8dd84560082426aee574948d9e.jpg",
        'img_class_3': "https://i.pinimg.com/564x/af/19/4b/af194baa4af245e816b2446202acc1ee.jpg",
        'img_class_4': "https://i.pinimg.com/564x/d0/41/55/d04155faa76f1501079a2135ffe3b853.jpg",
        'img_class_5': "https://i.pinimg.com/564x/4f/95/fd/4f95fd1d691a176704501259d2cb016f.jpg"
    },
    {
        'author': {
            'username': 'test-user'
        },
        'title': 'Cafe',
        'content': '카페 메뉴 사진 모음',
        'date_posted': datetime.strptime('2023-10-09', '%Y-%m-%d'),
        'img_title': "https://i.pinimg.com/564x/3a/72/80/3a7280a8fd049571d02274ca786d863c.jpg",
        'img_class_1': "https://i.pinimg.com/564x/3a/72/80/3a7280a8fd049571d02274ca786d863c.jpg",
        'img_class_2': "https://i.pinimg.com/564x/6e/e3/ef/6ee3ef51baaa198b7fd6754e72965151.jpg",
        'img_class_3': "https://i.pinimg.com/564x/f0/88/54/f088544f0c5b04fe1883a3c0dbe30300.jpg",
        'img_class_4': "https://i.pinimg.com/564x/af/34/21/af3421bdea685a4de3af9da4af978107.jpg",
        'img_class_5': "https://i.pinimg.com/564x/21/32/52/2132529e01d8c39ff02fc0edb81fa680.jpg"
    },
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=posts)

@app.route("/post")
def post():
    return render_template("post.html", posts=posts)

app.run(host="0.0.0.0", debug=True)

