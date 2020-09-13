# Flask Services
![Tests](https://github.com/jlsneto/flaskservice/workflows/Python%20Tests/badge.svg)
![PyPi Publish](https://github.com/jlsneto/flaskservice/workflows/PyPi%20Publish/badge.svg)
[![PyPI version](https://badge.fury.io/py/flaskservice.svg)](https://badge.fury.io/py/flaskservice)

## Get started
Install with pip

`pip install flaskservice`

or

`python -m pip install flaskservice`

## Example Code
```python
from flaskservice import Api, View

class ExampleView(View):
    # parameters of your flaskservice
    name: str = "Joab Leite" # it is not required because it has a defined value
    height: float # Required

    def get(self):
        print(self.name)
        return self.response(message=10)

    def post(self):
        return self.response(self.name)

api = Api(__name__)
api.add_view(ExampleView, urls="/example")

api.runserver(host='127.0.0.1', port=5000, debug=True)
```
Server is running on default port 5000 if not changed.
Send ``post`` or ``get`` and see result (:
