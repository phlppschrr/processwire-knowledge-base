# $field->getTemplates($getCount = false): TemplatesArray|int

Source: `wire/core/Field.php`

Return the list of of Templates using this field.

## Usage

~~~~~
// basic usage
$templatesArray = $field->getTemplates();

// usage with all arguments
$templatesArray = $field->getTemplates($getCount = false);
~~~~~

## Arguments

- `$getCount` (optional) `bool` Get count rather than FieldgroupsArray? (default=false) 3.0.182+

## Return value

- `TemplatesArray|int` WireArray of Template objects or count when requested.
