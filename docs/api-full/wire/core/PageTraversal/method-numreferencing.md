# $pageTraversal->numReferencing(Page $page, $field = false): int|array

Source: `wire/core/PageTraversal.php`

Return number of pages this one is following (referencing) by way of Page references

## Usage

~~~~~
// basic usage
$int = $pageTraversal->numReferencing($page);

// usage with all arguments
$int = $pageTraversal->numReferencing(Page $page, $field = false);
~~~~~

## Arguments

- `$page` `Page`
- `$field` (optional) `bool` Optionally limit to field, or specify boolean true to return array of counts per field.

## Return value

- `int|array`
