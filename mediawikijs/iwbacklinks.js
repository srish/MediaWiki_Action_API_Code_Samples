// This file is autogenerated. See modules.json and autogenerator.py for details

/*
	iwbacklinks.js

	MediaWiki API Demos
	Demo of `Iwbacklinks` module: Get pages linking to wikibooks:Main_Page.

	MIT License
*/

var params = {
		action: 'query',
		list: 'iwbacklinks',
		iwblprefix: 'wikibooks',
		iwbltitle: 'Main_Page',
		format: 'json'
	},
	api = new mw.Api();

api.get( params ).done( function ( data ) {
	console.log( data );
} );
