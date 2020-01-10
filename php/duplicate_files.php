<?php

/*
    duplicate_files.php

    MediaWiki API Demos
    Demo of `Duplicatefiles` module: List duplicates of the given files.

    MIT License
*/

$endPoint = "https://en.wikipedia.org/w/api.php";
$params = [
    "action" => "query",
    "titles" => "Image:1995.jpg|Image:Welcome.gif",
    "prop" => "duplicatefiles",
    "format" => "json"
];

$url = $endPoint . "?" . http_build_query( $params );

$ch = curl_init( $url );
curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
$output = curl_exec( $ch );
curl_close( $ch );

echo( $output );
