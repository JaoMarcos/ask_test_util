import json
from unittest import TestCase
import os

from ask_sdk_core.utils import is_request_type, is_intent_name
from dotenv import load_dotenv

load_dotenv()


from ask_test_util.ask_test_util import SkillTester
from dotenv import load_dotenv


from ask_sdk.standard import StandardSkillBuilder
sb = StandardSkillBuilder()

@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    print("LaunchRequest")
    speech_text = "Hello world"

    handler_input.response_builder.speak(speech_text)
    return handler_input.response_builder.response

@sb.request_handler(can_handle_func=is_intent_name("HelloWorldIntent"))
def hello_request_handler(handler_input):
    print(" HelloWorldIntent")
    speech_text = "HelloWorldIntent"

    handler_input.response_builder.speak(speech_text)
    return handler_input.response_builder.response


class TestInteractionModels(TestCase):
    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.client_id = os.environ["CLIENT_ID"]
        cls.client_secret = os.environ["CLIENT_SECRET"]
        cls.refresh_token = os.environ["refresh_token"]
        cls.skill_id = os.environ["SKILL_ID"]
        cls.default_location = os.environ["LOCATION"]
        cls.skill_tester = SkillTester(sb, location=cls.default_location,client_id=cls.client_id, client_secret=cls.client_secret,
                                        refresh_token=cls.refresh_token, skill_id=cls.skill_id,
                                        default_location=cls.default_location)



    def test_environment(self):
        launch_response = self.skill_tester.get_test_response("alexa open skill tester", None, sb)
        assert launch_response.event['request']['type'] == 'LaunchRequest'

        hello_response = self.skill_tester.get_test_response("alexa open skill tester", launch_response.event['session'], sb)
        assert hello_response.event['request']['type'] == 'IntentRequest'
        assert hello_response.event['request']['intent']['name'] == 'HelloWorldIntent'
