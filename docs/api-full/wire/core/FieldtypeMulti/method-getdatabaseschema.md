# $fieldtypeMulti->getDatabaseSchema(Field $field): array

Source: `wire/core/FieldtypeMulti.php`

Modify the default schema provided by Fieldtype to include a 'sort' field, and integrate that into the primary key.

## Usage

~~~~~
// basic usage
$array = $fieldtypeMulti->getDatabaseSchema($field);

// usage with all arguments
$array = $fieldtypeMulti->getDatabaseSchema(Field $field);
~~~~~

## Arguments

- `$field` `Field`

## Return value

- `array`
