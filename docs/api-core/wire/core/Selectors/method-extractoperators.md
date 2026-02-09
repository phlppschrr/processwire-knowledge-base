# $selectors->extractOperators(&$str): array

Source: `wire/core/Selectors.php`

Given a string starting with an operator, return that operator, and remove it from $str.

## Usage

~~~~~
// basic usage
$array = $selectors->extractOperators($str);

// usage with all arguments
$array = $selectors->extractOperators(&$str);
~~~~~

## Arguments

- `$str` `string`

## Return value

- `array`
