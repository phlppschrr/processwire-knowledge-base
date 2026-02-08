# $sanitizer->attrName($value, $maxLength = 255): string

Source: `wire/core/Sanitizer.php`

Sanitize to an ASCII-only HTML attribute name

## Usage

~~~~~
// basic usage
$string = $sanitizer->attrName($value);

// usage with all arguments
$string = $sanitizer->attrName($value, $maxLength = 255);
~~~~~

## Arguments

- `$value` `string`
- `$maxLength` (optional) `int`

## Return value

- `string`

## Since

3.0.133
