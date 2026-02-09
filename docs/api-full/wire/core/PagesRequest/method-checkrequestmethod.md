# $pagesRequest->checkRequestMethod(Page $page): bool

Source: `wire/core/PagesRequest.php`

Check current request method

## Usage

~~~~~
// basic usage
$bool = $pagesRequest->checkRequestMethod($page);

// usage with all arguments
$bool = $pagesRequest->checkRequestMethod(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Return value

- `bool` True if current request method allowed, false if not
