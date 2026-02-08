# $fieldtype->___createField(Field $field): bool

Source: `wire/core/Fieldtype.php`

Create a new field table in the database.

This method should execute the SQL query necessary to create $field->table
It should throw a WireException if failure occurs.
Most Fieldtype modules use this built-in implementation.

## Usage

~~~~~
// basic usage
$bool = $fieldtype->___createField($field);

// usage with all arguments
$bool = $fieldtype->___createField(Field $field);
~~~~~

## Arguments

- `$field` `Field`

## Return value

- `bool`

## Exceptions

- `WireException`
