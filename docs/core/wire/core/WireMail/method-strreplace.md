# $wireMail->strReplace($str, $find, $replace = ''): string

Source: `wire/core/WireMail.php`

Recursive string replacement

This is better than using str_replace() because it handles cases where replacement
results in the construction of a new $find that was not present in original $str.
Note: this function ignores case.

## Arguments

- `$str` `string`
- `$find` `string|array`
- `$replace` (optional) `string`

## Return value

string
