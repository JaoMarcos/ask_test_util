# ask_test_util Package
The ask_test_util package is a Python library that helps you test Alexa skills by simulating requests. It provides a
simple interface for automating the testing process without the need for human interaction or changing the skill
endpoint.

# Features
-   Simulates requests to an Alexa skill to test its behavior
-   Automates the testing process
-   Creates a similar 'handler_input' object that users can use to test the Lambda functions locally

# Installation
To install the ask_test_util package, run the following command:

``` pip install ask_test_util``` 

# Usage
To use the ask_test_util package, you first need to set up some environment variables with the necessary information.
You can either add the following data into the .env file or set them as environment variables.

```
SKILL_ID=
CLIENT_ID=
CLIENT_SECRET=
refresh_token=
LOCATION=  
```

You can find how to get those variable here: https://pypi.org/project/ask-smapi-sdk/


```python

import os
from dotenv import load_dotenv
from ask_test_util.skill_tester import SkillTester
from ask_sdk_model import SkillBuilder

# Use the same SkillBuilder you create on the lambda function
from lambda_function.lambda_function import sb


load_dotenv()
client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]
refresh_token = os.environ["refresh_token"]
skill_id = os.environ["SKILL_ID"]
default_location = os.environ["LOCATION"]
skill_tester = SkillTester(sb, location=default_location, client_id=client_id, client_secret=client_secret,
                                refresh_token=refresh_token, skill_id=skill_id,
                                default_location=default_location)

launch_response = skill_tester.get_test_response("alexa open skill tester", None, sb)
assert launch_response.event['request']['type'] == 'LaunchRequest'


hello_response = skill_tester.get_test_response("Hello", launch_response.event['session'], sb)
assert hello_response.event['request']['type'] == 'IntentRequest'
assert hello_response.event['request']['intent']['name'] == 'HelloWorldIntent'
```



