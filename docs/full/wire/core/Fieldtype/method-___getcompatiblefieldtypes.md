# $fieldtype->___getCompatibleFieldtypes(Field $field): Fieldtypes|null

Source: `wire/core/Fieldtype.php`

Get an array of Fieldtypes that are compatible with this one

This represents the list of Fieldtype modules that the user is allowed to change to from this one.

## Usage

~~~~~
// basic usage
$fieldtypes = $fieldtype->___getCompatibleFieldtypes($field);

// usage with all arguments
$fieldtypes = $fieldtype->___getCompatibleFieldtypes(Field $field);
~~~~~

## Arguments

- `$field` `Field`

## Return value

- `Fieldtypes|null`
