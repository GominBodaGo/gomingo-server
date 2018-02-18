from app import api_root
from flask_restful import Resource, marshal_with
from flask import request
from app.model.User import User
from app.model.Token import Token
from app.api.v1.marshaling.login_status_result import login_status_result
from app import db
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime, timedelta
import hashlib


@api_root.resource("/v1/login")
class Login(Resource):

    @marshal_with(login_status_result)
    def post(self):
        try:

            json_data = request.get_json(force=True)
            username = json_data['username']
            password = json_data['password']
            now = datetime.now()

            due_date = str(now + timedelta(hours=3))
            due_date_hashSHA = hashlib.sha256()
            due_date_hashSHA.update(due_date.encode('utf-8'))
            hash_date = due_date_hashSHA.hexdigest()

            try:

                user = User.query.filter(User.username == username).one()

                join_date = str(user.joinDate.strftime("%y/%m/%d"))

                password_hashSHA = hashlib.sha256()
                password_hashSHA.update((password + join_date).encode('utf-8'))
                password = password_hashSHA.hexdigest()
                print(password + "hello")

            except NoResultFound:

                join_date = datetime.now().strftime("%y/%m/%d")
                join_date = str(join_date)

                password_hashSHA = hashlib.sha256()
                password_hashSHA.update((password + join_date).encode('utf-8'))
                password = password_hashSHA.hexdigest()
                print(password + "joined")
                user = User(username=username, password=password, joinDate=join_date)

                db.session.add(user)
                db.session.commit()

            if user.password != password:
                return None, 403
            else:
                token = Token(token=hash_date, dueDate=due_date, userId=user.id)

                db.session.add(token)
                db.session.commit()
                return token

        except Exception:
            return None, 400