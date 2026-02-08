# $sanitizer->punyDecodeName($value, $version = 0): string

Source: `wire/core/Sanitizer.php`

Decode a PW-punycode'd name value

## Usage

~~~~~
// basic usage
$string = $sanitizer->punyDecodeName($value);

// usage with all arguments
$string = $sanitizer->punyDecodeName($value, $version = 0);
~~~~~

## Arguments

- `$value` `string`
- `$version` (optional) `int` 0=auto-detect, 1=original/buggy, 2=punycode library, 3=php idn function

## Return value

- `string`
