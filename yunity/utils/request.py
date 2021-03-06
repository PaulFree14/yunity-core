from json import loads as load_json

from django.test import RequestFactory

from yunity.utils.misc import json_stringify
from yunity.utils.validation import HasKey


class Parameter(object):
    def __init__(self, name, validator=None):
        self.name = name
        self.validator = validator or HasKey(name)


class JsonRequestFactory(RequestFactory):
    def post(self, path, data=None, **kwargs):
        return super().post(
            path=path,
            data=json_stringify(data),
            content_type='application/json; charset=utf-8',
        )


class JsonRequest(object):
    def __init__(self, http_request, json_body):
        self._http_request = http_request
        self._json_body = json_body

    @classmethod
    def from_http_request(cls, http_request):
        """
        :type http_request: HttpRequest
        :rtype: JsonRequest
        :raises ValueError: if the request body is not valid JSON

        """
        try:
            json_data = load_json(http_request.body.decode("utf-8"))
        except ValueError:
            raise ValueError('incorrect json request')

        return cls(http_request, json_data)

    def __getattr__(self, item):
        if item == 'body':
            return self._json_body
        return getattr(self._http_request, item)
