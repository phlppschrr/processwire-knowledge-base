# $markupFieldtype->renderValue($value): string

Source: `wire/core/MarkupFieldtype.php`

Render the entire $page->get($field->name) value.

Classes descending from MarkupFieldtype this would implement their own method.

## Usage

~~~~~
// basic usage
$string = $markupFieldtype->renderValue($value);
~~~~~

## Arguments

- `$value` `mixed` The unformatted value to render.

## Return value

- `string`
