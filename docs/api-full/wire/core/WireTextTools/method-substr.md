# $wireTextTools->substr($str, $start, $length = null): string

Source: `wire/core/WireTextTools.php`

Get part of a string

## Usage

~~~~~
// basic usage
$string = $wireTextTools->substr($str, $start);

// usage with all arguments
$string = $wireTextTools->substr($str, $start, $length = null);
~~~~~

## Arguments

- `$str` `string`
- `$start` `int`
- `$length` (optional) `int|null` Max chars to use from str. If omitted or NULL, extract all characters to the end of the string.

## Return value

- `string`

## See Also

- [https://www.php.net/manual/en/function.substr.php](https://www.php.net/manual/en/function.substr.php)
