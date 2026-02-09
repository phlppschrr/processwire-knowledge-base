# FieldsetPage

Source: `wire/modules/Fieldtype/FieldtypeRepeater/FieldsetPage.php`

Inherits: `RepeaterPage`

## Summary

FieldsetPage represents Page objects used by the FieldtypeFieldsetPage module

Common methods:
- [`trackChange()`](method-trackchange.md)
- [`get()`](method-get.md)
- [`getOf()`](method-getof.md)
- [`getUnformatted()`](method-getunformatted.md)
- [`getFormatted()`](method-getformatted.md)

## Methods
- [`trackChange(string $what, mixed $old = null, mixed $new = null): $this`](method-trackchange.md) Track a change to a property in this object
- [`get(string $key): mixed`](method-get.md) Get a property
- [`getOf(string $key, bool $of): mixed`](method-getof.md) Get property in formatted (true) or unformatted (false) state
- [`getUnformatted(string $key): mixed`](method-getunformatted.md) Get the unformatted value of a field, regardless of current output formatting state
- [`getFormatted(string $key): mixed`](method-getformatted.md) Get the formatted value of a field, regardless of output formatting state
- [`getForPage(): Page`](method-getforpage.md) Return the page that this repeater item is for
- [`getForField(): Field`](method-getforfield.md) Return the field that this repeater item belongs to
