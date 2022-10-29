import sqlalchemy as db
from flask import Flask
from flask import request


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
engine = db.create_engine("cockroachdb://root:@localhost:32412/defaultdb")
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
    return "Done"


@app.route('/user/qna/<user_email>', methods=['GET'])
def get_user_qna(user_email):
    return "Done"


@app.route('/qna', methods=['POST'])
def create_qna():
    print(request.json)
    qna = QnA(**request.json)
    print(qna.question)
    return "Done"


@app.route('/qna', methods=['PUT'])
def update_qna():
    print(request.json)
    qna = QnA(**request.json)
    print(qna.question)
    return "Done"


@app.route('/qna', methods=['GET'])
def get_qna():
    return "Done"


if __name__ == "__main__":
    app.run(debug=True)
