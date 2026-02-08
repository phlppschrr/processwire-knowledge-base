# $page->hasChildren($selector = true): int

Source: `wire/core/Page.php`

Return the number of visible children, optionally with conditions

This method is similar to `$page->numChildren()` except that the default behavior is to exclude non-visible children.

This method may be more convenient for front-end navigation use than the `$page->numChildren()` method because
it only includes the count of visible children. By visible, we mean children that are not hidden, unpublished,
or non-accessible due to access control.

## Example

~~~~~
// Determine if we should show navigation to children
if($page->hasChildren()) {
  // Yes, we should show navigation to children
}
~~~~~

## Usage

~~~~~
// basic usage
$int = $page->hasChildren();

// usage with all arguments
$int = $page->hasChildren($selector = true);
~~~~~

## Arguments

- `$selector` (optional) `bool|string|array` - When not specified, result is quantity of visible children (excludes unpublished, hidden, no-access, etc.) - When a string or array, a selector is assumed and quantity will be counted based on selector. - When boolean true, number includes only visible children (this is the default behavior, so no need to specify this value). - When boolean false, number includes all children without conditions, including unpublished, hidden, no-access, etc.

## Return value

- `int` Number of children
