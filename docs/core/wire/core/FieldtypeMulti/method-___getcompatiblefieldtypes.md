# $fieldtypeMulti->getCompatibleFieldtypes(Field $field): Fieldtypes|null

Source: `wire/core/FieldtypeMulti.php`

Get an array of Fieldtypes that are compatible with this one (i.e. ones the user may change the type to)

## Usage

~~~~~
// basic usage
$fieldtypes = $fieldtypeMulti->getCompatibleFieldtypes($field);

// usage with all arguments
$fieldtypes = $fieldtypeMulti->getCompatibleFieldtypes(Field $field);
~~~~~

## Hookable

- Hookable method name: `getCompatibleFieldtypes`
- Implementation: `___getCompatibleFieldtypes`
- Hook with: `$fieldtypeMulti->getCompatibleFieldtypes()`

## Arguments

- `$field` `Field` Just in case it's needed

## Return value

- `Fieldtypes|null`
