# $sanitizer->maxBytes($value, $maxBytes = 128): string

Source: `wire/core/Sanitizer.php`

Limit bytes used by given string to max specified

- This function will not break multibyte characters so long as PHP has mb_string.
- This function works only with strings and if given a non-string it will be converted to one.

## Usage

~~~~~
// basic usage
$string = $sanitizer->maxBytes($value);

// usage with all arguments
$string = $sanitizer->maxBytes($value, $maxBytes = 128);
~~~~~

## Arguments

- `$value` `string`
- `$maxBytes` (optional) `int`

## Return value

- `string`

## Since

3.0.125
