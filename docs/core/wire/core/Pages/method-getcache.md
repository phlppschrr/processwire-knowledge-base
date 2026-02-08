# $pages->getCache($id = null): Page|array|null

Source: `wire/core/Pages.php`

Given a Page ID, return it if it's cached, or NULL of it's not.

If no ID is provided, then this will return an array copy of the full cache.

You may also pass in the string "id=123", where 123 is the page_id

## Usage

~~~~~
// basic usage
$page = $pages->getCache();

// usage with all arguments
$page = $pages->getCache($id = null);
~~~~~

## Arguments

- `$id` (optional) `int|string|null`

## Return value

- `Page|array|null`
