# $pageValues->getBracketValue(Page $page, $key, $value = null): array|mixed|Page|PageArray|Wire|WireArray|WireData|string|\Traversable

Source: `wire/core/PageValues.php`

Get value that ends with square brackets to get iterable value, filtered value or property value

~~~~~
$iterableValue = $page->get('field_name[]');
~~~~~
Note: When requesting an iterable value, this method will return an empty array in cases where
the Page::get() method would return null.

## Arguments

- `$page` `Page`
- `$key` `string`
- `$value` (optional) `mixed` Value to use rather than pulling from $page

## Return value

array|mixed|Page|PageArray|Wire|WireArray|WireData|string|\Traversable
