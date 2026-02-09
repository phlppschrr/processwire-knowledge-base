# $fieldgroups->getFieldNames($fieldgroup): array

Source: `wire/core/Fieldgroups.php`

Get all field names used by given fieldgroup

Use this when you want to identify the field names (or IDs) without loading the fieldgroup or fields in it.

## Usage

~~~~~
// basic usage
$array = $fieldgroups->getFieldNames($fieldgroup);
~~~~~

## Arguments

- `$fieldgroup` `string|int|Fieldgroup` Fieldgroup name, ID or object

## Return value

- `array` Returned array of field names indexed by field ID

## Since

3.0.194
