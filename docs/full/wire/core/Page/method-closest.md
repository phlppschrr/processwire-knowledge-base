# $page->closest($selector): Page|NullPage

Source: `wire/core/Page.php`

Find the closest parent page matching your selector

This is like `$page->parent()` but includes the current Page in the possible pages that can be matched,
and the $selector argument is required.

## Usage

~~~~~
// basic usage
$page = $page->closest($selector);
~~~~~

## Arguments

- `$selector` `string|array` Selector string to match.

## Return value

- `Page|NullPage` $selector Returns the current Page or closest parent matching the selector. Returns NullPage when no match.
