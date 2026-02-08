# $field->getFieldgroups($getCount = false): FieldgroupsArray|int

Source: `wire/core/Field.php`

Return the list of Fieldgroups using this field.

## Usage

~~~~~
// basic usage
$fieldgroupsArray = $field->getFieldgroups();

// usage with all arguments
$fieldgroupsArray = $field->getFieldgroups($getCount = false);
~~~~~

## Arguments

- `$getCount` (optional) `bool` Get count rather than FieldgroupsArray? (default=false) 3.0.182+

## Return value

- `FieldgroupsArray|int` WireArray of Fieldgroup objects or count if requested
