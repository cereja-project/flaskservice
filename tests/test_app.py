import unittest
from flaskservice import Api, View
from cereja import console


class ExampleView(View):
    # parameters of your flaskservice
    name: str = "Joab Leite"  # it is not required because it has a defined value
    other_param: str

    def post(self):
        return self.response(result={'name': self.name, 'other_param': self.other_param})


class TestData(unittest.TestCase):
    def setUp(self):
        self.api = Api('Test Api')
        self.urls = ('/test', '/test2')
        self.api.add_view(ExampleView, urls=self.urls)
        self.client = self.api.app.test_client

    def test_endpoints_diponibiliry(self):
        for url in self.urls:
            msg = f"""endpoint ({url}). Expected 200 'OK'"""
            res = self.client().post(url, data={'name': 'john', 'other_param': 'test'})
            console.log(str(res.json))
            self.assertEqual(200, res.status_code, msg)
