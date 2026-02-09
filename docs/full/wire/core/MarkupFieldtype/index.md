# MarkupFieldtype

Source: `wire/core/MarkupFieldtype.php`

Inherits: `WireData`
Implements: `Module`

Class MarkupFieldtype

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

Methods:
- [`__construct(?Page $page = null, ?Field $field = null, mixed $value = null)`](method-__construct.md)
- [`render(string $property = ''): string`](method-render.md)
- [`renderValue(mixed $value): string`](method-rendervalue.md)
- [`renderProperty(string $property, mixed $value): string`](method-renderproperty.md)
- [`valueToString(mixed $value, bool $encode = true): string`](method-valuetostring.md)
- [`arrayToString(array|WireArray $value, bool $encode = true): string`](method-arraytostring.md)
- [`objectToString(Wire|object $value): string`](method-objecttostring.md)
- [`renderInputfieldValue($value): string`](method-renderinputfieldvalue.md)
- [`isLinkablePageProperty(Page $page, $property): bool`](method-islinkablepageproperty.md)
- [`__toString(): string`](method-__tostring.md)
- [`setValue($value)`](method-setvalue.md)
- [`getValue(): mixed`](method-getvalue.md)
