from app import api_root
from flask_restful import Resource, marshal_with

from app.helper.util import get_token_row
from app.model.Item import Item
from app.api.v1.marshaling.search_result import search_result
from flask import request
from urllib import parse

@api_root.resource("/v1/search/products")
class Create(Resource):

    @marshal_with(search_result)
    @get_token_row()
    def get(self, token):
        title = request.args.get('title')
        title = parse.unquote(title)
        result = Item.query.filter(Item.name.like("%"+ title + "%")).limit(15).all()
        return result

    def post(self):
        return "This is Post request."