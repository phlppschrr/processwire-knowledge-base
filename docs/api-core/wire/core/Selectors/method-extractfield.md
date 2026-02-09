# $selectors->extractField(&$str): string

Source: `wire/core/Selectors.php`

Given a string starting with a field, return that field, and remove it from $str.

## Usage

~~~~~
// basic usage
$string = $selectors->extractField($str);

// usage with all arguments
$string = $selectors->extractField(&$str);
~~~~~

## Arguments

- `$str` `string`

## Return value

- `string`
