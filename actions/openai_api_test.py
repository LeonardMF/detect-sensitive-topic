import unittest
from actions.openai_api import request_gpt


class TestOpenaiAPI(unittest.TestCase):

    def test_request_gpt(self):
        
        gpt_response = request_gpt("I have a chronic pain, could you advise something?")

        self.assertEqual(gpt_response,"yes")    