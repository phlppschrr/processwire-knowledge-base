# $pageTraversal->references(Page $page, $selector = '', $field = '', $getCount = false): PageArray|array|int

Source: `wire/core/PageTraversal.php`

Return pages that are referencing the given one by way of Page references

## Usage

~~~~~
// basic usage
$items = $pageTraversal->references($page);

// usage with all arguments
$items = $pageTraversal->references(Page $page, $selector = '', $field = '', $getCount = false);
~~~~~

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|bool` Optional selector to filter results by or boolean true as shortcut for `include=all`.
- `$field` (optional) `Field|string` Limit to follower pages using this field, - or specify boolean TRUE to make it return array of PageArrays indexed by field name.
- `$getCount` (optional) `bool` Specify true to return counts rather than PageArray(s)

## Return value

- `PageArray|array|int`

## Exceptions

- `WireException` Highly unlikely
