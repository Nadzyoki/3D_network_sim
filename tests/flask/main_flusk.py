from flask import Flask
from flask import request

app = Flask(__name__)

name_server = "My server"
listPc = {"first":"mypc","second":"motherPc"}

list_user = {}

@app.route("/", methods=['GET'])
def sample():
    return 'Get method'

@app.route("/name_server/")
def ret():
    return name_server

@app.route("/list_pc/")
def listOfPc():
    return listPc

@app.route("/calc/", methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        a = int(request.form['a'])
        b = int(request.form['b'])
        result = a + b
        return f'{a} + {b} = {result}'
    return f'Был получен {request.method} запрос.'

@app.route("/newuser/", methods=["POST"])
def new_user():
    a = request.form['name']
    b = request.form['pos']
    list_user[a] = b
    return None

@app.route("/mypos/", methods=["POST"])
def ret_pos():
    name = request.form['name']
    return list_user[name]

@app.route("/newpos/", methods=["POST"])
def new_pos():
    name = request.form['name']
    old = list_user[name]
    x = request.form['x']
    y = request.form['y']
    list_user[name]=(x,y)
    print(f"old pos {old}")
    print(f"new pos {list_user[name]}")
    return None

data = (
    dict(name='Python', released='20.01.1991'),
    dict(name='Java', released='23.06.1995'),
    dict(name='GO', released='10.11.2009'),
)

@app.route('/table/', methods=['GET'])
def table():
    start = '<html><body><table border=1>'
    caption = '<caption>Языки программирования</caption>'
    header = '<tr><th>Название</th><th>Первый релиз</th></tr>'
    end = '</table></body></html>'
    tr_list = list()
    for item in data:
        tr_list.append(
            f'<tr><td>{item["name"]}</td><td>{item["released"]}</td></tr>'
        )
    content = ''.join(tr_list)
    html_response = ''.join((start, caption, header, content, end))
    return html_response.format(request.method)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000')