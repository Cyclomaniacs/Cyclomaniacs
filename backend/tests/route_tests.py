import unittest
import requests


class TestEndpoints(unittest.TestCase):
    def test_server_connection(self):
        response = requests.get('http://127.0.0.1:5000/')
        self.assertEqual(response.status_code, 200)
        
    # def test_ip_locator(self):
    #     response = requests.get('http://127.0.0.1:5000/')
    #     self.assertEqual(response.json()['blogs'][0]['name'], 'Hurricane 101')


if __name__ == '__main__':
    unittest.main()