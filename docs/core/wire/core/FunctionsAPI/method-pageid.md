# $functionsAPI->pageId($value): int|false

Source: `wire/core/FunctionsAPI.php`

Return id for given page or false if it’s not a page

Returns positive int (page id) for page that exists, 0 for NullPage,
or false if given $value is not a Page.

## Arguments

- Page|mixed $value

## Return value

int|false

## Meta

- @since 3.0.224
