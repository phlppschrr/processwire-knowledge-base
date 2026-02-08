# $pageTraversal->hasReferences(Page $page, $selector = '', $field = ''): int|array

Source: `wire/core/PageTraversal.php`

Return number of VISIBLE pages that are following (referencing) the given one by way of Page references

Note that this excludes hidden, unpublished and otherwise non-accessible pages (access control).
If you do not want to exclude these, use the numFollowers() function instead, OR specify "include=all" for
the $selector argument.

## Usage

~~~~~
// basic usage
$int = $pageTraversal->hasReferences($page);

// usage with all arguments
$int = $pageTraversal->hasReferences(Page $page, $selector = '', $field = '');
~~~~~

## Arguments

- `$page` `Page`
- `$selector` (optional) `string` Filter count by this selector
- `$field` (optional) `string|Field|bool` Limit count to given Field or specify boolean true to return array of counts.

## Return value

- `int|array` Returns count, or array of counts (if $field==true)
