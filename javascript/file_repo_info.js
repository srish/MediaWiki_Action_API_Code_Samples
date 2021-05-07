//This file is autogenerated. See modules.json and autogenerator.py for details

const fetch = require("node-fetch");

/*
    file_repo_info.js

    MediaWiki API Demos
    Demo of `Filerepoinfo` module: Get information about file repositories.

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "query",
    meta: "filerepoinfo",
    friprop: "url|name|displayname",
    format: "json"
};

url = url + "?origin=*";
Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});

fetch(url)
    .then(function(response){return response.json();})
    .then(function(response) {console.log(response);})
    .catch(function(error){console.log(error);});
