# $fieldtypeMulti->___getCompatibleFieldtypes(Field $field): Fieldtypes|null

Source: `wire/core/FieldtypeMulti.php`

Get an array of Fieldtypes that are compatible with this one (i.e. ones the user may change the type to)

## Usage

~~~~~
// basic usage
$fieldtypes = $fieldtypeMulti->___getCompatibleFieldtypes($field);

// usage with all arguments
$fieldtypes = $fieldtypeMulti->___getCompatibleFieldtypes(Field $field);
~~~~~

## Arguments

- `$field` `Field` Just in case it's needed

## Return value

- `Fieldtypes|null`
