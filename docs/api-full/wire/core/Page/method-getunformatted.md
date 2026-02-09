# $page->getUnformatted($key): mixed

Source: `wire/core/Page.php`

Get the unformatted value of a field, regardless of current output formatting state

When a page’s output formatting state is off, `$page->get('property')` or `$page->property` will
produce the same result as this method call.

## Example

~~~~~
// Get the 'body' field without any text formatters applied
$body = $page->getUnformatted('body');
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->getUnformatted($key);
~~~~~

## Arguments

- `$key` `string` Field or property name to retrieve

## Return value

- `mixed`

## See Also

- [Page::getFormatted()](method-getformatted.md)
- [Page::of()](method-of.md)
- [Page::setOutputFormatting()](index.md)
- [Page::outputFormatting()](index.md)
