// This file is autogenerated. See modules.json and autogenerator.py for details

/*
	geosearch.js

	MediaWiki API Demos
	Demo of `Geosearch` module: Search for wiki pages nearby

	MIT License
*/

var params = {
		action: 'query',
		list: 'geosearch',
		gscoord: '37.7891838|-122.4033522',
		gsradius: '10000',
		gslimit: '10',
		format: 'json'
	},
	api = new mw.Api();

api.get( params ).done( function ( data ) {
	var pages = data.query.geosearch,
		place;
	for ( place in pages ) {
		console.log( pages[ place ].title );
	}
} );
