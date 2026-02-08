# $pageTraversal->numReferences(Page $page, $selector = '', $field = ''): int|array

Source: `wire/core/PageTraversal.php`

Return number of ANY pages that are following (referencing) the given one by way of Page references

## Arguments

- `$page` `Page`
- `$selector` (optional) `string` Filter count by this selector
- `$field` (optional) `string|Field|bool` Limit count to given Field or specify boolean true to return array of counts.

## Return value

int|array Returns count, or array of counts (if $field==true)
