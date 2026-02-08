# $page->getFormatted($key): mixed

Source: `wire/core/Page.php`

Get the formatted value of a field, regardless of output formatting state

When a page's output formatting state is on, `$page->get('property')` or `$page->property` will
produce the same result as this method call.

~~~~~
// Get the formatted 'body' field (text formatters applied)
$body = $page->getFormatted('body');
~~~~~

## Arguments

- string $key Field or property name to retrieve

## Return value

mixed

## See also

- [Page::getUnformatted()](method-getunformatted.md)
- [Page::of()](method-of.md)
