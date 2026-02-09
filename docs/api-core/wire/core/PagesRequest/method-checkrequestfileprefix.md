# $pagesRequest->checkRequestFilePrefix(&$path): bool

Source: `wire/core/PagesRequest.php`

Check for secured filename: method 2 (deprecated)

Used only if $config->pagefileUrlPrefix is defined

## Usage

~~~~~
// basic usage
$bool = $pagesRequest->checkRequestFilePrefix($path);

// usage with all arguments
$bool = $pagesRequest->checkRequestFilePrefix(&$path);
~~~~~

## Arguments

- `$path` `string`

## Return value

- `bool`
