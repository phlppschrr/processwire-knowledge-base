# $wireTextTools->trim($str, $chars = ''): string

Source: `wire/core/WireTextTools.php`

Strip whitespace (or other characters) from the beginning and end of a string

## Usage

~~~~~
// basic usage
$string = $wireTextTools->trim($str);

// usage with all arguments
$string = $wireTextTools->trim($str, $chars = '');
~~~~~

## Arguments

- `$str` `string`
- `$chars` (optional) `string` Omit for default

## Return value

- `string`
