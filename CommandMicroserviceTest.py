# test_api.py

import unittest
import json
from app import app

class CommandMicroserviceTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_git_command(self):
        response = self.app.post(
            '/classify',
            data=json.dumps({"command": "git status"}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"type": "git"})

    def test_docker_command(self):
        response = self.app.post(
            '/classify',
            data=json.dumps({"command": "docker run nginx"}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"type": "docker"})

    def test_unknown_command(self):
        response = self.app.post(
            '/classify',
            data=json.dumps({"command": "foo --bar"}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"type": "unknown"})

    def test_missing_command_field(self):
        response = self.app.post(
            '/classify',
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

if __name__ == '__main__':
    unittest.main()
