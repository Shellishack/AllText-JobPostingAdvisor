async function getgroup(jobreq) {
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  // I dont know why Azure AutoML wants an extra column???
  var raw = JSON.stringify({
    "data": [
      {
        "jobrequirements": jobreq,
        "Column4":0
      }
    ]
  });

  var requestOptions = {
    method: 'POST',
    body: raw,
    headers: myHeaders
  };
  
  let response= await fetch("https://jobpostinghandleserver.azurewebsites.net/getgroup", requestOptions);
  return response;
}

async function getbias(jobreq) {
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  // I dont know why Azure AutoML wants an extra column???
  var raw = JSON.stringify({
    "data": [
      {
        "jobrequirements": jobreq,
        "Column4":0
      }
    ]
  });

  var requestOptions = {
    method: 'POST',
    body: raw,
    headers: myHeaders
  };
  let response=await fetch("https://jobpostinghandleserver.azurewebsites.net/getbias", requestOptions);
  return response;
}

export { getbias, getgroup };