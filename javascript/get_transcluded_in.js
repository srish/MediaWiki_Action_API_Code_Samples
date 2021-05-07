//This file is autogenerated. See modules.json and autogenerator.py for details

const fetch = require("node-fetch");

/*
    get_transcluded_in.js

    MediaWiki API Demos
    Demo of `Transcludedin` module: Get a list of pages which transclude a given page

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "query",
    titles: "Main Page",
    prop: "transcludedin",
    format: "json"
};

url = url + "?origin=*";
Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});

fetch(url)
    .then(function(response){return response.json();})
    .then(function(response) {console.log(response);})
    .catch(function(error){console.log(error);});
