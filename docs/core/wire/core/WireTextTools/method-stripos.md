# $wireTextTools->stripos($haystack, $needle, $offset = 0): bool|false|int

Source: `wire/core/WireTextTools.php`

Find the position of the first occurrence of a case-insensitive substring in a string

## Usage

~~~~~
// basic usage
$bool = $wireTextTools->stripos($haystack, $needle);

// usage with all arguments
$bool = $wireTextTools->stripos($haystack, $needle, $offset = 0);
~~~~~

## Arguments

- `$haystack` `string`
- `$needle` `string`
- `$offset` (optional) `int`

## Return value

- `bool|false|int`

## See Also

- [https://www.php.net/manual/en/function.stripos.php](https://www.php.net/manual/en/function.stripos.php)
