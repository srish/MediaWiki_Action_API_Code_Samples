//This file is autogenerated. See modules.json and autogenerator.py for details

/*
    check_token.js

    MediaWiki API Demos
    Demo of `Checktoken` module: Get request to check a CSRF token.

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "checktoken",
    token: "123ABC",
    type: "csrf",
    format: "json"
};

url = url + "?origin=*";
Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});

fetch(url)
    .then(function(response){return response.json();})
    .then(function(response) {console.log(response);})
    .catch(function(error){console.log(error);});
