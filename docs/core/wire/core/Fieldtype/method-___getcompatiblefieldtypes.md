# $fieldtype->getCompatibleFieldtypes(Field $field): Fieldtypes|null

Source: `wire/core/Fieldtype.php`

Get an array of Fieldtypes that are compatible with this one

This represents the list of Fieldtype modules that the user is allowed to change to from this one.

## Usage

~~~~~
// basic usage
$fieldtypes = $fieldtype->getCompatibleFieldtypes($field);

// usage with all arguments
$fieldtypes = $fieldtype->getCompatibleFieldtypes(Field $field);
~~~~~

## Hookable

- Hookable method name: `getCompatibleFieldtypes`
- Implementation: `___getCompatibleFieldtypes`
- Hook with: `$fieldtype->getCompatibleFieldtypes()`

## Arguments

- `$field` `Field`

## Return value

- `Fieldtypes|null`
