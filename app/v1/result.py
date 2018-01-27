from flask_restful import fields

hello_result = {
    'title': fields.String(default="haha!"),
    'des': fields.String
}