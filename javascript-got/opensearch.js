
const got = require("got");

/*
    opensearch.js

    MediaWiki API Demos
    Demo of `Opensearch` module: Search the wiki and obtain
	results in an OpenSearch (http://www.opensearch.org) format

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 


async function opensearch(url, searchTerm) {

    var params = {
        action: "opensearch",
        search: searchTerm,
        limit: "5",
        namespace: "0",
        format: "json"
    };

    try {
    
        const response = await got(url, {
            searchParams: params
        }).json()

        console.log( response );
    } catch( error ) {
        console.log( error.response.body );
    }
}


opensearch(url, "Hampi");
