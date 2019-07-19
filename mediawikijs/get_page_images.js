// This file is autogenerated. See modules.json and autogenerator.py for details

/*
	get_page_images.js

	MediaWiki API Demos
	Demo of `Images` module: Send a GET request to obtain a JSON
	object listing all of the image files embedded on a single page

	MIT License
*/

var params = {
		action: 'query',
		prop: 'images',
		titles: 'Albert Einstein',
		format: 'json'
	},
	api = new mw.Api();

api.get( params ).done( function ( data ) {
	var pages = data.query.pages,
		page;
	for ( page in pages ) {
		pages[ page ].images.forEach( function ( img ) {
			console.log( img.title );
		} );
	}
} );
