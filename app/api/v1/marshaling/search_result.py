from flask_restful import fields

search_result = {
    'name': fields.String(default="haha!"),
    'price': fields.Integer,
    'cate' : fields.String(attribute='categoryRow.name')
}



