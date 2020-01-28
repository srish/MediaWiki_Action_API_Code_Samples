/*
	deleted_revisions.js

	MediaWiki API Demos
	Demo of `Deletedrevisions` module: Get a list of deleted revisions for Talk:Main Page.

	MIT License
*/

var params = {
		action: 'query',
		titles: 'Talk:Main_Page',
		prop: 'deletedrevisions',
		drvprop: 'user|comment|content',
		drvslots: '*',
		format: 'json'
	},
	api = new mw.Api();

api.get( params ).done( function ( data ) {
	console.log( data );
} );
