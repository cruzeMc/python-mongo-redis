import unittest

import requests

import app.controller.sample_controller


class MyTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_universities(self):
        req = requests.get(url='http://127.0.0.1:5000/universities?country=Jamaica')
        universities = req.json()
        actual = len(universities)
        expected = 3
        self.assertEqual(actual, expected)

    def test_get_universities2(self):
        with app.test_request_context():
            out = controller.get_universities()
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
