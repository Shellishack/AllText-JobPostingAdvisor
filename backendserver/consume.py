import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context


def get_result_bias(jobrequirement):
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

    # Request data goes here
    # Column4 is an extra column. I dont know why Azure AutoML generates it???
    data = {
        "data":
        [
            {
                'jobrequirements': jobrequirement,
                'Column4':0
            },
        ],
    }

    body = str.encode(json.dumps(data))

    url = 'http://e83e850b-edc8-4106-9fca-3ae284381cda.eastus.azurecontainer.io/score'
    api_key = '' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        print(result)
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))

    return result

def get_result_group(jobrequirement):
    allowSelfSignedHttps(True)

    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

    # Request data goes here
    # Column4 is an extra column. I dont know why Azure AutoML generates it???
    data = {
        "data":
        [
            {
                'jobrequirements': jobrequirement
            },
        ],
    }

    body = str.encode(json.dumps(data))

    url = 'http://bfde2cfb-3b5e-40da-830c-292873a36ed7.eastus.azurecontainer.io/score'
    api_key = '' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        print(result)
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))

    return result

# get_result()