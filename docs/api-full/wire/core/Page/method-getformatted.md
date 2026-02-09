# $page->getFormatted($key): mixed

Source: `wire/core/Page.php`

Get the formatted value of a field, regardless of output formatting state

When a page's output formatting state is on, `$page->get('property')` or `$page->property` will
produce the same result as this method call.

## Example

~~~~~
// Get the formatted 'body' field (text formatters applied)
$body = $page->getFormatted('body');
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->getFormatted($key);
~~~~~

## Arguments

- `$key` `string` Field or property name to retrieve

## Return value

- `mixed`

## See Also

- [Page::getUnformatted()](method-getunformatted.md)
- [Page::of()](method-of.md)
