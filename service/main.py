from service.base import Api, View


class ExampleView(View):
    name: str
    height: float

    def get(self):
        print(self.name)
        return self.response(message=10)

    def post(self):
        return self.response(self.name)


api = Api(__name__)
api.add_view(ExampleView, urls='/')
if __name__ == "__main__":
    api.runserver(host='127.0.0.1', debug=True)
