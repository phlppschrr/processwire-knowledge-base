# $page->links($selector = '', $field = ''): PageArray

Source: `wire/core/Page.php`

Return pages linking to this one (in Textarea/HTML fields)

Applies only to Textarea fields with “html” content-type and link abstraction enabled.

## Usage

~~~~~
// basic usage
$items = $page->links();

// usage with all arguments
$items = $page->links($selector = '', $field = '');
~~~~~

## Hookable

- Hookable method name: `links`
- Implementation: `___links`
- Hook with: `$page->links()`

## Arguments

- `$selector` (optional) `string|bool` Optional selector to filter by or boolean true for “include=all”. (default='')
- `$field` (optional) `string|Field` Optionally limit results to specified field. (default=all applicable Textarea fields)

## Return value

- `PageArray`

## Since

3.0.107
