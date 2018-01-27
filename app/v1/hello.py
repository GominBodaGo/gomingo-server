from app import api_root
from flask_restful import Resource

@api_root.resource("/v1/chaeeun/<input_string>")
class Create(Resource):
    def get(self, input_string):
        return "your input is" + input

    def post(self):
        return "This is Post request."