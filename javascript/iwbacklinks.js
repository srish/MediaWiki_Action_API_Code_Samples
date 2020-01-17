//This file is autogenerated. See modules.json and autogenerator.py for details

/*
    iwbacklinks.js

    MediaWiki API Demos
    Demo of `Iwbacklinks` module: Get pages linking to wikibooks:Main_Page.

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "query",
    list: "iwbacklinks",
    iwblprefix: "wikibooks",
    iwbltitle: "Main_Page",
    format: "json"
};

url = url + "?origin=*";
Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});

fetch(url)
    .then(function(response){return response.json();})
    .then(function(response) {console.log(response);})
    .catch(function(error){console.log(error);});
