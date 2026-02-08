# $field->setFieldtype($type): Field

Source: `wire/core/Field.php`

Set what type of field this is (Fieldtype).

## Usage

~~~~~
// basic usage
$field = $field->setFieldtype($type);
~~~~~

## Arguments

- `$type` `string|Fieldtype` Type should be either a Fieldtype object or the string name of a Fieldtype object.

## Return value

- `Field` $this

## Exceptions

- `WireException`
