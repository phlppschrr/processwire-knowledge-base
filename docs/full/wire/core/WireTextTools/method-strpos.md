# $wireTextTools->strpos($haystack, $needle, $offset = 0): bool|false|int

Source: `wire/core/WireTextTools.php`

Find position of first occurrence of string in a string

## Usage

~~~~~
// basic usage
$bool = $wireTextTools->strpos($haystack, $needle);

// usage with all arguments
$bool = $wireTextTools->strpos($haystack, $needle, $offset = 0);
~~~~~

## Arguments

- `$haystack` `string`
- `$needle` `string`
- `$offset` (optional) `int`

## Return value

- `bool|false|int`

## See Also

- [https://www.php.net/manual/en/function.strpos.php](https://www.php.net/manual/en/function.strpos.php)
