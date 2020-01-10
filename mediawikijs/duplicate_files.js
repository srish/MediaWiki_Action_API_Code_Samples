/*
	duplicate_files.js

    MediaWiki API Demos
    Demo of `Duplicatefiles` module: List duplicates of the given files.

    MIT License
*/

var params = {
    action: "query",
    titles: "Image:1995.jpg|Image:Welcome.gif",
    prop: "duplicatefiles",
    format: "json"
},
api = new mw.Api();

api.get( params ).done( function ( data ) {
console.log( data );
} );
