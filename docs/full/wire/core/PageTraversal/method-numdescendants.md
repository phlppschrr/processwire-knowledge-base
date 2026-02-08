# $pageTraversal->numDescendants(Page $page, $selector = null): int

Source: `wire/core/PageTraversal.php`

Return number of descendants, optionally with conditions

Use this over $page->numDescendants property when you want to specify a selector or when you want the result to
include only visible descendants. See the options for the $selector argument.

## Arguments

- `$page` `Page`
- `$selector` (optional) `bool|string|int|array` When not specified, result includes all descendants without conditions, same as $page->numDescendants property. When a string or array, a selector is assumed and quantity will be counted based on selector. When boolean true, number includes only visible descendants (excludes unpublished, hidden, no-access, etc.) When boolean false, number includes all descendants without conditions, including unpublished, hidden, no-access, etc. When integer 1 number includes viewable descendants (as opposed to visible, viewable includes hidden pages + it also includes unpublished pages if user has page-edit permission).

## Return value

int Number of descendants
