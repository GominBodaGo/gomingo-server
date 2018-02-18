from app import api_root
from flask_restful import Resource, marshal_with

from app.helper.util import get_token_row
from app.model.Receipt import Receipt
from app.model.Token import Token
from flask import request
from datetime import datetime, timedelta
from app import db
from sqlalchemy.orm.exc import NoResultFound


from app.api.v1.marshaling.group_payment_status_result import group_payment_status_result


@api_root.resource("/v1/sms_receipt")
class Payment(Resource):

    @marshal_with(group_payment_status_result)
    @get_token_row()
    def post(self, token):
        json_data = request.get_json(force=True)
        storeName = json_data['storeName']
        price = json_data['price']
        paymentDate = datetime.now()
        categoryId = 1


        user = token.userId

        temp_item_row = Receipt(storeName=storeName, price=price, paymentDate=paymentDate, userId=user,
                                categoryId=categoryId)

        db.session.add(temp_item_row)
        db.session.commit()

        result = Receipt.query.filter(Receipt.categoryId == categoryId).filter(
            Receipt.paymentDate.between(paymentDate - timedelta(hours=1), paymentDate + timedelta(hours=1))).all()

        temp_item_row.count = len(result)
        return temp_item_row
