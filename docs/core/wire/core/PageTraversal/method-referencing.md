# $pageTraversal->referencing(Page $page, $field = false, $getCount = false): PageArray|int|array

Source: `wire/core/PageTraversal.php`

Return pages that this page is referencing by way of Page reference fields

## Arguments

- `$page` `Page`
- `$field` (optional) `bool|Field|string|int` Limit results to requested field, or specify boolean true to return array indexed by field names.
- `$getCount` (optional) `bool` Specify true to return count(s) rather than pages.

## Return value

PageArray|int|array
