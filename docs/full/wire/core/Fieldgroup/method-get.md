# $fieldgroup->get($key): Field|string|int|null|array

Source: `wire/core/Fieldgroup.php`

Get a Fieldgroup property or a Field.

It is preferable to use `Fieldgroup::getField()` to retrieve fields from the Fieldgroup because
the scope of this `get()` method means it can return more than just Field object.

## Usage

~~~~~
// basic usage
$field = $fieldgroup->get($key);
~~~~~

## Arguments

- `$key` `string|int` Property name to retrieve, or Field name

## Return value

- `Field|string|int|null|array`
