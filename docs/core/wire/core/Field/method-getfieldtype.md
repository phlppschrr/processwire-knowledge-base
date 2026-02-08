# $field->getFieldtype(): Fieldtype|null|string

Source: `wire/core/Field.php`

Return the Fieldtype module representing this field’s type.

Can also be accessed directly via `$field->type`.

## Usage

~~~~~
// basic usage
$fieldtype = $field->getFieldtype();
~~~~~

## Return value

- `Fieldtype|null|string`

## Since

3.0.16 Added for consistency, but all versions can still use $field->type.
