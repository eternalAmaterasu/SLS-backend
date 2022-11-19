import json
import sys

import sqlalchemy as db
from flask import Flask
from flask import request

from weather.RoutingBase import RoutingBase


class UserDetail:
    def __init__(self, email, password, **kwargs):
        self.email = email
        self.password = password
        if 'name' in kwargs:
            self.name = kwargs['name']

    def __repr__(self):
        return json.dumps(self.__dict__)


class QnA:
    def __init__(self, id, question, options):
        self.id = id
        self.question = question
        self.options = options

    def __repr__(self):
        return json.dumps(self.__dict__)


class Answers:
    def __init__(self, email, id, response):
        self.email = email
        self.id = id
        self.response = response

    def __repr__(self):
        return json.dumps(self.__dict__)


app = Flask(__name__)
print("Firing up db connection from the server")

engine = db.create_engine(f"cockroachdb://root:@{sys.argv[1]}:{sys.argv[2]}/{sys.argv[3]}",
                          connect_args={'connect_timeout': 20})
conn = engine.connect()
print("DB connected!")
md = db.MetaData()
user_detail_ds = db.Table('user_detail', md, autoload=True, autoload_with=engine)
qna_ds = db.Table('qna', md, autoload=True, autoload_with=engine)
answers_ds = db.Table('answers', md, autoload=True, autoload_with=engine)


@app.route('/')
def base_location():
    return "Ikuze, It's working"


@app.route('/user/detail', methods=['POST'])
def create_user_detail():
    print(request.json)
    user = UserDetail(**request.json)

    print("Prepping sql stmt")
    row = user_detail_ds.insert().values(
        name=user.name,
        email=user.email,
        password=user.password
    )
    print(f"Executing sql: {row}")
    conn.execute(row)

    return f"Insertion of data of {user.name} done"


@app.route('/user/detail', methods=['PUT'])
def update_user_detail():
    print(request.json)
    user = UserDetail(**request.json)

    print("Prepping sql stmt")
    row = user_detail_ds.insert().values(
        name=user.name,
        email=user.email,
        password=user.password
    )
    print(f"Executing sql: {row}")
    conn.execute(row)

    return f"Update of data of {user.name} done"


@app.route('/user/detail/<user_id>', methods=['GET'])
def get_user_detail(user_id):
    row = user_detail_ds.select().where(user_detail_ds.c.email == user_id)
    result = conn.execute(row)
    user = None
    for res in result:
        user = UserDetail(res[0], res[1], name=f"{res[2]}")
        break

    print(user.__dict__)
    return user.__dict__


@app.route('/user/detail/verify', methods=['POST'])
def verify_user_detail():
    user = UserDetail(**request.json)
    row = user_detail_ds.select() \
        .where(user_detail_ds.c.email == user.email) \
        .where(user_detail_ds.c.password == user.password)
    result = conn.execute(row)
    found = False
    for res in result:
        print(res)
        found = True
        break
    return f"User '{user.email}' exist status: {found}"


@app.route('/qna', methods=['POST'])
def create_qna():
    qna = QnA(**request.json)
    row = qna_ds.insert().values(
        id=qna.id,
        question=qna.question,
        options=qna.options
    )
    print(f"Going to execute sql: {row}")
    conn.execute(row)
    print("Execution done")
    return "Done"


@app.route('/qna/<id>', methods=['GET'])
def get_qna(id):
    row = qna_ds.select().where(qna_ds.c.id == id)
    result = conn.execute(row)
    for row in result:
        return QnA(row[0], row[1], row[2]).__repr__()
    return "Not found"


@app.route('/qna/', methods=['GET'])
def get_all_qna():
    row = qna_ds.select()
    result = conn.execute(row)
    qna = [QnA(row[0], row[1], row[2]) for row in result]
    return str(qna)


@app.route('/answers', methods=['POST'])
def create_answer():
    answer = Answers(**request.json)
    row = answers_ds.insert().values(
        email=answer.email,
        id=answer.id,
        response=answer.response
    )
    conn.execute(row)
    print(answer.response)
    return "Done adding"


@app.route('/answers', methods=['PUT'])
def update_answer():
    answer = Answers(**request.json)
    row = answers_ds.update() \
        .where(answers_ds.c.email == answer.email) \
        .where(answers_ds.c.id == answer.id) \
        .values(question=answer.response)
    conn.execute(row)
    return "Done updating"


@app.route('/answers/<email>/<id>', methods=['GET'])
def get_answer(email, id):
    row = answers_ds.select() \
        .where(answers_ds.c.email == email) \
        .where(answers_ds.c.id == id)
    result = conn.execute(row)
    for row in result: return Answers(*row).__repr__()
    return "Not found"


@app.route('/answers/', methods=['GET'])
def get_all_answers():
    row = answers_ds.select()
    result = conn.execute(row)
    print(result)
    answer_list = [Answers(row[0], row[1], row[2]) for row in result]
    data = {
        "answers": answer_list
    }
    return data.__repr__()


@app.route('/weather/<location>', methods=['GET'])
def get_weather(location):
    routing_base = RoutingBase()
    weather_data = routing_base.fetch_weather_from_upstream(location)
    routing_base = None  # force clearing memory
    return weather_data


if __name__ == "__main__":
    app.run(debug=True)
