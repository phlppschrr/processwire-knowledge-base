# $field->setSetupName($setupName = null): string

Source: `wire/core/Field.php`

Set setup name from Fieldtype to apply when field is saved

## Usage

~~~~~
// basic usage
$string = $field->setSetupName();

// usage with all arguments
$string = $field->setSetupName($setupName = null);
~~~~~

## Arguments

- `$setupName` (optional) `string` Setup name or omit to instead get the current value

## Return value

- `string` Returns current value
