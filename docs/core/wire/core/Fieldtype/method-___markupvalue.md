# $fieldtype->___markupValue(Page $page, Field $field, $value = null, $property = ''): string|MarkupFieldtype

Source: `wire/core/Fieldtype.php`

Render a markup string of the value.

Non-markup components should also be entity encoded where appropriate.

Most Fieldtypes don't need to implement this since the default covers most scenarios.

This is different from `Fieldtype::formatValue()` in that it always returns a string (or object that can be
typecast to a string) that is output ready with markup. Further, this method may be used to render
specific properties in compound Fieldtypes. The intention here is primarily for admin output purposes,
but can be used front-end where applicable.

This is different from `Inputfield::renderValue()` in that the context may be outside that of an Inputfield,
as Inputfields can have external CSS or JS dependencies.

## Usage

~~~~~
// basic usage
$string = $fieldtype->___markupValue($page, $field);

// usage with all arguments
$string = $fieldtype->___markupValue(Page $page, Field $field, $value = null, $property = '');
~~~~~

## Arguments

- `$page` `Page` Page that $value comes from
- `$field` `Field` Field that $value comes from
- `$value` (optional) `mixed` Optionally specify the value returned by `$page->getFormatted('field')`. When specified, value must be a formatted value. If null or not specified (recommended), it will be retrieved automatically.
- `$property` (optional) `string` Optionally specify the property or index to render. If omitted, entire value is rendered.

## Return value

- `string|MarkupFieldtype` Returns a string or object that can be output as a string, ready for output. Return a MarkupFieldtype value when suitable so that the caller has potential specify additional config options before typecasting it to a string.
