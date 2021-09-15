from task import app
from lesson1.utils import SkyproTestCase


class TestCase(SkyproTestCase):

    def get_key(self):
        return "173645"

    def test_route(self):
        with app.app_context():
            address = "/"
            app.testing = True
            response = app.test_client().get(address)

        self.assertEqual(response.status_code, 200, msg = "Запрос не обрабатывается")
        self.assertEqual(response.data, b'It works!', msg = "Роут возвращает ok")
