from flask import request
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound

from app.model.Token import Token

def get_token_row():
    def wrap(func):
        def wrapper(resource, *args, **kwargs):
            now = datetime.now()
            token = request.headers.get('token')

            try:

                token_query = Token.query.filter(Token.token == token).filter(
                    Token.dueDate > now
                )

                token = token_query.one()

            except NoResultFound:

                raise Exception("")


            return func(resource, token, *args, **kwargs)

        return wrapper
    return wrap

