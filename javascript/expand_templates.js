//This file is autogenerated. See modules.json and autogenerator.py for details

const fetch = require("node-fetch");

/*
    expand_templates.js

    MediaWiki API Demos
    Demo of `Expandtemplates` module: Obtain general site info.

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "expandtemplates",
    text: "{{Project:Sandbox}}",
    prop: "wikitext",
    format: "json"
};

url = url + "?origin=*";
Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});

fetch(url)
    .then(function(response){return response.json();})
    .then(function(response) {console.log(response);})
    .catch(function(error){console.log(error);});
