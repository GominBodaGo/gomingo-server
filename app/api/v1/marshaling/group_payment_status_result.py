from flask_restful import fields

cate = {
    'id' : fields.Integer,
    'name' : fields.String
}


group_payment_status_result = {
    'category': fields.Nested(cate, attribute='categoryRow'),
    'storeName': fields.String(default="haha!"),
    'price': fields.Integer,
    'count': fields.Integer
}


