import sys

import sqlalchemy as db
from flask import Flask
from flask import request

from weather import RoutingBase


class UserDetail:
    def __init__(self, email, password, **kwargs):
        self.email = email
        self.password = password
        if 'name' in kwargs:
            self.name = kwargs['name']


class UserQnA:
    def __init__(self, email, qna):
        self.email = email
        self.qna = qna


class QnA:
    def __init__(self, id, question):
        self.id = id
        self.question = question


app = Flask(__name__)
print("Firing up db connection from the server")
engine = db.create_engine(f"cockroachdb://root:@{sys.argv[1]}:{sys.argv[2]}/{sys.argv[3]}")
conn = engine.connect()
print("DB connected!")
md = db.MetaData()
user_detail_ds = db.Table('user_detail', md, autoload=True, autoload_with=engine)
user_qna_ds = db.Table('user_qna', md, autoload=True, autoload_with=engine)
qna_ds = db.Table('qna', md, autoload=True, autoload_with=engine)


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


@app.route('/user/qna', methods=['POST'])
def update_user_qna():
    user_qna = UserQnA(**request.json)
    row = user_qna_ds.insert().values(
        email=user_qna.email,
        qna=user_qna.qna
    )
    conn.execute(row)
    print(user_qna.qna)
    return "Done"


@app.route('/user/qna/<user_email>', methods=['GET'])
def get_user_qna(user_email):
    row = user_qna_ds.select().where(user_qna_ds.c.email == user_email)
    result = conn.execute(row)
    user_qna = None
    for row in result:
        user_qna = UserQnA(user_email, row.qna)
        return user_qna.__dict__

    return "Not found"


@app.route('/qna', methods=['POST'])
def create_qna():
    qna = QnA(**request.json)
    row = qna_ds.insert().values(
        id=qna.id,
        question=qna.question
    )
    conn.execute(row)
    print(qna.question)
    return "Done adding"


@app.route('/qna', methods=['PUT'])
def update_qna():
    qna = QnA(**request.json)
    row = qna_ds.update().where(qna_ds.c.id == qna.id).values(
        question=qna.question
    )
    conn.execute(row)
    return "Done updating"


@app.route('/qna', methods=['GET'])
def get_qna():
    qna_list = []
    row = qna_ds.select()
    result = conn.execute(row)
    print(result)
    [qna_list.append(UserQnA(row[0], row[1]).__dict__) for row in result]

    data = {
        "qna_list": qna_list
    }
    return data


@app.route('/weather/<location>', methods=['GET'])
def get_weather(location):
    return RoutingBase.fetch_weather_from_upstream(location)


if __name__ == "__main__":
    app.run(debug=True)
