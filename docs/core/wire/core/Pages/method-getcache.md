# $pages->getCache($id = null): Page|array|null

Source: `wire/core/Pages.php`

Given a Page ID, return it if it's cached, or NULL of it's not.

If no ID is provided, then this will return an array copy of the full cache.

You may also pass in the string "id=123", where 123 is the page_id

## Arguments

- int|string|null $id

## Return value

Page|array|null
