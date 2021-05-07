//This file is autogenerated. See modules.json and autogenerator.py for details

const fetch = require('node-fetch');

/*
    get_exturlusage.js

    MediaWiki API Demos
    Demo of `Exturlusage` module: Enumerate pages that contain a given URL.

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "query",
    format: "json",
    list: "exturlusage",
    euquery: "slashdot.org"
};

url = url + "?origin=*";
Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});

fetch(url)
    .then(function(response){return response.json();})
    .then(function(response) {
        var exturls = response.query.exturlusage;
        for (var exturl in exturls) {
            console.log("Page " + exturls[exturl].title + " has " + exturls[exturl].url + " url.");
        }
    })
    .catch(function(error){console.log(error);});
