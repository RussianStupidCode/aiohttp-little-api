from aiohttp import web
import jsonschema
from aiohttp import hdrs, BasicAuth


class BaseMixin:
    def _get_item_id(self):
        return int(self.request.match_info["item_id"])

    @staticmethod
    def _get_not_found():
        response = web.json_response({'message': 'not found'})
        response.set_status(404)
        return response

    @staticmethod
    def _get_bad_luck():
        response = web.json_response({'message': 'Bad luck'})
        response.set_status(400)
        return response

    @staticmethod
    def validate(data, schema):
        try:
            jsonschema.validate(
                instance=data, schema=schema,
            )
        except jsonschema.ValidationError as e:
            raise e