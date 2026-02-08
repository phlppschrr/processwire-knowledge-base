# $fieldSelectorInfo->getOperators($inputType = ''): array

Source: `wire/core/FieldSelectorInfo.php`

Get array of operators

## Usage

~~~~~
// basic usage
$array = $fieldSelectorInfo->getOperators();

// usage with all arguments
$array = $fieldSelectorInfo->getOperators($inputType = '');
~~~~~

## Arguments

- `$inputType` (optional) `string` Specify: number, text, fulltext or select, or omit to return all possible operators at once

## Return value

- `array` of operators or blank array if invalid type specified
