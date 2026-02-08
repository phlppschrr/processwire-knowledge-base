# $sanitizer->punyDecodeName($value, $version = 0): string

Source: `wire/core/Sanitizer.php`

Decode a PW-punycode'd name value

## Arguments

- `$value` `string`
- `$version` (optional) `int` 0=auto-detect, 1=original/buggy, 2=punycode library, 3=php idn function

## Return value

string
