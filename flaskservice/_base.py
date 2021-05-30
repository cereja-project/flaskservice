import sys
from typing import Union

from flask.json import jsonify
from flask_restful import Resource, inputs
from flask_restful.reqparse import RequestParser
from werkzeug.exceptions import InternalServerError, MethodNotAllowed, HTTPException
import logging
from flask import Flask
from flask_cors import CORS
from flask_restful import Api as _Api

logger = logging.getLogger(__name__)

__all__ = ['View', 'Api']


class View(Resource):
    """
    Base Resource is the base of any and all end-points that may be created in the api.
    It defines the HTTP methods available for implementation.
    The methods are defined to handle each HTTP request, as well as the functionality that will be executed.

    You must implement the methods you want to use, to do so just overwrite the implementation of your service.
    """

    def __init__(self, **kwargs):
        self.request_parser = RequestParser(bundle_errors=True)
        for arg, _type in self.__annotations__.items():
            _type = inputs.boolean if _type is bool else _type
            if not hasattr(self, arg):
                self.request_parser.add_argument(arg, type=_type, required=True)
                continue
            self.request_parser.add_argument(arg, type=_type, default=getattr(self, arg))
        super().__init__(**kwargs)
        for arg in self.request_parser.parse_args(strict=True).items():
            self.__setattr__(*arg)

    @classmethod
    def _unlock(cls):
        cls.__locked = False

    def post(self):
        raise MethodNotAllowed()

    def get(self):
        raise MethodNotAllowed()

    def put(self):
        raise MethodNotAllowed()

    def patch(self):
        raise MethodNotAllowed()

    def delete(self):
        raise MethodNotAllowed()

    def __init_subclass__(cls, **kwargs):
        # check type hint and default values
        for arg, _type in cls.__annotations__.items():
            if not hasattr(cls, arg):
                continue
            assert type(getattr(cls, arg)) is _type, f'Param type error: {arg}:{_type} != {type(getattr(cls, arg))}'

    def response(self, *args, **kwargs):
        return jsonify(*args, **kwargs)


class _CustomApi(_Api):
    def handle_error(self, e):
        if not isinstance(e, HTTPException):
            exc_type, exc_value, tb = sys.exc_info()
            e = InternalServerError(description=f'{exc_type.__name__}: {exc_value}')
        return super(_CustomApi, self).handle_error(e)


T_View = type(View)


class Api:
    def __init__(self, name: str):
        self._name = name
        self._app = Flask(name)
        self._cors = CORS(self._app, resources={r"*": {"origins": "*"}})
        self._api = _CustomApi(self._app)

    @property
    def app(self):
        return self._app

    @property
    def name(self):
        return self._name

    @property
    def cors(self):
        return self._cors

    def add_view(self, view: T_View, urls: Union[str, list, tuple] = '/', **kwargs):
        assert issubclass(view, View), 'Send class reference of <View>'
        urls = (urls,) if isinstance(urls, str) else urls
        self._api.add_resource(view, *urls, **kwargs)

    def runserver(self, host=None, port=5000, debug=None, load_dotenv=True, **options):
        self._app.run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)
