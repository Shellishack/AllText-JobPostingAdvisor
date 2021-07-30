function getgroup(jobreq){
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  var raw = JSON.stringify({
    "data": [
      {
        "jobrequirements": jobreq
      }
    ]
  });

  var requestOptions = {
    method: 'POST',
    body:raw,
    headers: myHeaders
  };

  fetch("https://jobpostinghandleserver.azurewebsites.net/getgroup", requestOptions)
    .then(response => response.text())
    .then(result => console.log(JSON.parse(result)))
    .catch(error => console.log('error', error));
}

function getbias(jobreq){
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  var raw = JSON.stringify({
    "data": [
      {
        "jobrequirements": jobreq
      }
    ]
  });

  var requestOptions = {
    method: 'POST',
    body:raw,
    headers: myHeaders
  };

  fetch("https://jobpostinghandleserver.azurewebsites.net/getbias", requestOptions)
    .then(response => response.text())
    .then(result => console.log(JSON.parse(result)))
    .catch(error => console.log('error', error));
}
