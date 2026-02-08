# $wireTextTools->strripos($haystack, $needle, $offset = 0): bool|false|int

Source: `wire/core/WireTextTools.php`

Find the position of the last occurrence of a case-insensitive substring in a string

## Usage

~~~~~
// basic usage
$bool = $wireTextTools->strripos($haystack, $needle);

// usage with all arguments
$bool = $wireTextTools->strripos($haystack, $needle, $offset = 0);
~~~~~

## Arguments

- `$haystack` `string`
- `$needle` `string`
- `$offset` (optional) `int`

## Return value

- `bool|false|int`

## See Also

- [https://www.php.net/manual/en/function.strripos.php](https://www.php.net/manual/en/function.strripos.php)
