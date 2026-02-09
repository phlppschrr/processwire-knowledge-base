# $page->numDescendants($selector = null): int

Source: `wire/core/Page.php`

Return number of descendants (children, grandchildren, great-grandchildren, …), optionally with conditions

Use this over the `$page->numDescendants` property when you want to specify a selector or apply
some other filter to the result (see options for `$selector` argument). If you want to include only
visible descendants specify a selector (string or array) or boolean true for the `$selector` argument,
if you don’t need a selector.

If you want to find descendant pages (rather than count), use the `Page::find()` method.

## Example

~~~~~
// Find how many descendants were modified in the last week
$qty = $page->numDescendants("modified>='-1 WEEK'");
~~~~~

## Usage

~~~~~
// basic usage
$int = $page->numDescendants();

// usage with all arguments
$int = $page->numDescendants($selector = null);
~~~~~

## Arguments

- `$selector` (optional) `bool|string|array` - When not specified, result includes all descendants without conditions, same as $page->numDescendants property. - When a string or array, a selector is assumed and quantity will be counted based on selector. - When boolean true, number includes only visible descendants (excludes unpublished, hidden, no-access, etc.)

## Return value

- `int` Number of descendants

## See Also

- [Page::numChildren()](method-numchildren.md)
- [Page::find()](method-find.md)
