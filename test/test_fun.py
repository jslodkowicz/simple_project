import sys
sys.path.append('..') # noqa
from weather import app
import unittest
import json


class FunTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home(self):
        resp = self.app.get('/')

        self.assertEqual(resp.status_code, 200)

    def test_json(self):
        resp = self.app.get('/json')

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            json.loads(resp.get_data()),
            {"message": "what's your weather?"}
        )


if __name__ == '__main__':
    unittest.main(verbosity=3)
