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


@app.route('/')
def base_location():
    return "Ikuze, It's working"


@app.route('/user/detail', methods=['POST'])
def create_user_detail():
    print(request.json)
    user = UserDetail(**request.json)
    return f"Insertion of data of {user.name} done"


@app.route('/user/detail', methods=['PUT'])
def update_user_detail():
    print(request.json)
    user = UserDetail(**request.json)
    return f"Update of data of {user.name} done"


@app.route('/user/detail/<user_id>', methods=['GET'])
def get_user_detail(user_id):
    return "Done"


@app.route('/user/detail/verify', methods=['POST'])
def verify_user_detail():
    user = UserDetail(**request.json)
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
