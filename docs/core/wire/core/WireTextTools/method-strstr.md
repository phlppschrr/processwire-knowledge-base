# $wireTextTools->strstr($haystack, $needle, $beforeNeedle = false): false|string

Source: `wire/core/WireTextTools.php`

Find the first occurrence of a string

## Usage

~~~~~
// basic usage
$result = $wireTextTools->strstr($haystack, $needle);

// usage with all arguments
$result = $wireTextTools->strstr($haystack, $needle, $beforeNeedle = false);
~~~~~

## Arguments

- `$haystack` `string`
- `$needle` `string`
- `$beforeNeedle` (optional) `bool` Return part of haystack before first occurrence of the needle? (default=false)

## Return value

- `false|string`

## See Also

- [https://www.php.net/manual/en/function.strstr.php](https://www.php.net/manual/en/function.strstr.php)
