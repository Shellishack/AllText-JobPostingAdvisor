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

    url = 'http://3fbf162c-2df3-40fd-9d95-f97bcc77c431.eastus.azurecontainer.io/score'
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
                'jobrequirements': jobrequirement,
                'Column4': 0
            },
        ],
    }

    body = str.encode(json.dumps(data))

    url = 'http://ef8d3d43-499b-4235-a41b-96b5677f585b.eastus.azurecontainer.io/score'
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