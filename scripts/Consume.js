
data = {
    "data":
    [
        {
            'jobrequirements': "Attention to detail and high level of accuracy",
        },
    ],
}

api_key = ""
url = 'http://7d115c1b-89ef-4be0-9040-c57be657da02.eastus.azurecontainer.io/score'
const testpara={
    headers:{'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)},
    body:data,
    method: "POST"
}


fetch(url,testpara)
    .then(res=> console.log(res))
