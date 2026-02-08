# $page->getUnformatted($key): mixed

Source: `wire/core/Page.php`

Get the unformatted value of a field, regardless of current output formatting state

When a page’s output formatting state is off, `$page->get('property')` or `$page->property` will
produce the same result as this method call.

~~~~~
// Get the 'body' field without any text formatters applied
$body = $page->getUnformatted('body');
~~~~~

## Arguments

- string $key Field or property name to retrieve

## Return value

mixed

## See also

- [Page::getFormatted()](method-getformatted.md)
- [Page::of()](method-of.md)
- [Page::setOutputFormatting()](index.md)
- [Page::outputFormatting()](index.md)
