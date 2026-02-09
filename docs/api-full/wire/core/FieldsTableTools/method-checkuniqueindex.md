# $fieldsTableTools->checkUniqueIndex(Field $field, $verbose = true)

Source: `wire/core/FieldsTableTools.php`

Check state of field unique 'data' index and update as needed

## Usage

~~~~~
// basic usage
$result = $fieldsTableTools->checkUniqueIndex($field);

// usage with all arguments
$result = $fieldsTableTools->checkUniqueIndex(Field $field, $verbose = true);
~~~~~

## Arguments

- `$field` `Field`
- `$verbose` (optional) `bool` Show messages when changes made? (default=true)

## Exceptions

- `WireException`
