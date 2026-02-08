# $fieldgroups->fieldRemoved(Fieldgroup $fieldgroup, Field $field)

Source: `wire/core/Fieldgroups.php`

Hook called when field has been removed from fieldgroup

## Usage

~~~~~
// basic usage
$result = $fieldgroups->fieldRemoved($fieldgroup, $field);

// usage with all arguments
$result = $fieldgroups->fieldRemoved(Fieldgroup $fieldgroup, Field $field);
~~~~~

## Hookable

- Hookable method name: `fieldRemoved`
- Implementation: `___fieldRemoved`
- Hook with: `$fieldgroups->fieldRemoved()`

## Arguments

- `$fieldgroup` `Fieldgroup`
- `$field` `Field`

## Since

3.0.193
