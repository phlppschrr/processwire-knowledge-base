# $markupFieldtype->renderProperty($property, $value): string

Source: `wire/core/MarkupFieldtype.php`

Render the just a property from the $page->get($field->name) value.

Applicable only if the value of the field is an array or object.

Classes descending from MarkupFieldtype would implement their own method.

## Usage

~~~~~
// basic usage
$string = $markupFieldtype->renderProperty($property, $value);
~~~~~

## Arguments

- `$property` `string` The property name being rendered.
- `$value` `mixed` The value of the property.

## Return value

- `string`
