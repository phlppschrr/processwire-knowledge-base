# $pageTraversal->references(Page $page, $selector = '', $field = '', $getCount = false): PageArray|array|int

Source: `wire/core/PageTraversal.php`

Return pages that are referencing the given one by way of Page references

## Arguments

- Page $page
- string|bool $selector Optional selector to filter results by or boolean true as shortcut for `include=all`.
- Field|string $field Limit to follower pages using this field, - or specify boolean TRUE to make it return array of PageArrays indexed by field name.
- bool $getCount Specify true to return counts rather than PageArray(s)

## Return value

PageArray|array|int

## Throws

- WireException Highly unlikely
