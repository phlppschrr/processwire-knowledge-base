# $field->setName($name): Field

Source: `wire/core/Field.php`

Set the field’s name

This method will throw a WireException when field name is a reserved word, is already in use,
is a system field, or is in some format not accepted for a field name.

## Arguments

- `$name` `string`

## Return value

Field $this

## Throws

- WireException
