# $page->findOne($selector = '', $options = array()): Page|NullPage

Source: `wire/core/Page.php`

Find one descendant page matching given selector

This is the same as `Pages::findOne()` except that the match is always a descendant of page it is called on.

## Example

~~~~~
// Find the most recently modified descendant page
$item = $page->findOne("sort=-modified");
~~~~~

## Usage

~~~~~
// basic usage
$page = $page->findOne();

// usage with all arguments
$page = $page->findOne($selector = '', $options = array());
~~~~~

## Arguments

- `$selector` (optional) `string|array` Selector string or array
- `$options` (optional) `array` Optional options to modify default bheavior, see options for `Pages::find()`.

## Return value

- `Page|NullPage` Returns Page when found, or NullPage when nothing found.

## See Also

- [Pages::findOne()](../Pages/method-findone.md)
- [Page::child()](method-child.md)

## Since

3.0.116
