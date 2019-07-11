//This file is autogenerated. See modules.json and autogenerator.py for details

/*
    get_redirects.js

    MediaWiki API Demos
    Demo of `Redirects` module: Get all redirects to the given page(s)

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "query",
    titles: "Jacques Kallis",
    prop: "redirects",
    format: "json"
};

url = url + "?origin=*";
Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});

fetch(url)
    .then(function(response){return response.json();})
    .then(function(response) {
        var pages = response.query.pages;
        for (var page in pages) {
            for (var redirects of pages[page].redirects) {
                console.log(redirects.title + " redirect to " + pages[page].title );
            }
        }
    })
    .catch(function(error){console.log(error);});
