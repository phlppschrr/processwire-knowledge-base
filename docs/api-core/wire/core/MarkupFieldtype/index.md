# MarkupFieldtype

Source: `wire/core/MarkupFieldtype.php`

Inherits: `WireData`
Implements: `Module`

## Summary

Class MarkupFieldtype

Common methods:
- [`render()`](method-render.md)
- [`renderValue()`](method-rendervalue.md)
- [`renderProperty()`](method-renderproperty.md)
- [`valueToString()`](method-valuetostring.md)
- [`arrayToString()`](method-arraytostring.md)

Provides pre-packaged markup rendering for Fieldtypes
and potentially serves as a module type. This base class
just provides generic rendering for various differnet types,
accommodating just about any Fieldtype. But it is built to be
extended for more specific needs in various Fieldtypes.

USAGE:

$m = new MarkupFieldtype($page, $field, $value);
echo $m->render();

// Alternate usage:
$m = new MarkupFieldtype();
$m->setPage($page);
$m->setField($field);
$m->setValue($value);
echo $m->render();

// Render just a specific property:
echo $m->render('property');

## Methods
- [`__construct(?Page $page = null, ?Field $field = null, mixed $value = null)`](method-__construct.md) Construct the MarkupFieldtype
- [`render(string $property = ''): string`](method-render.md) Render markup for the field or for the property from field
- [`renderValue(mixed $value): string`](method-rendervalue.md) Render the entire $page->get($field->name) value.
- [`renderProperty(string $property, mixed $value): string`](method-renderproperty.md) Render the just a property from the $page->get($field->name) value.
- [`valueToString(mixed $value, bool $encode = true): string`](method-valuetostring.md) Convert any value to a string
- [`arrayToString(array|WireArray $value, bool $encode = true): string`](method-arraytostring.md) Render an unknown array or WireArray to a string
- [`objectToString(Wire|object $value): string`](method-objecttostring.md) Render an object to a string
- [`renderInputfieldValue($value): string`](method-renderinputfieldvalue.md) Render a value using an Inputfield's renderValue() method
- [`isLinkablePageProperty(Page $page, $property): bool`](method-islinkablepageproperty.md) Is the given page property/field name one that should be linked to the source page in output?
- [`__toString(): string`](method-__tostring.md) The string value of a MarkupFieldtype is always the fully rendered field
- [`setValue($value)`](method-setvalue.md) Set the value
- [`getValue(): mixed`](method-getvalue.md) Get the value
