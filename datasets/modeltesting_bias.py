import urllib.request
import json
import os
import ssl
import pandas

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

validationset=pandas.read_csv('./automated_data/processed_data_testing_biasonly.csv')
# Request data goes here
data = {
    "data":
    [
    ],
}

for x in range(len(validationset)):
    data['data'].append({'jobrequirements':validationset.at[x,'jobrequirements'],'Column4':0})

# print(data)

body = str.encode(json.dumps(data))

url = 'http://e83e850b-edc8-4106-9fca-3ae284381cda.eastus.azurecontainer.io/score'
api_key = '' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    result=json.loads(json.loads(result.decode('utf8').replace("'",'"')))
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))

nwrong=0
lstwrong=[]
for x in range(len(result['result'])):
    if int(result['result'][x])!=int(validationset.at[x,'bias']):
        nwrong+=1
        lstwrong.append(validationset.iloc[x])

print("Wrong prediction:",nwrong)
print("Accuracy rate:",(len(validationset)-nwrong)/len(validationset))
