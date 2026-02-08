# $selectors->getOperatorsFromField(&$field): array

Source: `wire/core/Selectors.php`

Extract and return operator from end of field name, as used by selector arrays

## Usage

~~~~~
// basic usage
$array = $selectors->getOperatorsFromField($field);

// usage with all arguments
$array = $selectors->getOperatorsFromField(&$field);
~~~~~

## Arguments

- `$field` `string`

## Return value

- `array`
