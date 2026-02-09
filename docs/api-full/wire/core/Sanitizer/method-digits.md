# $sanitizer->digits($value, $maxLength = 1024): string

Source: `wire/core/Sanitizer.php`

Sanitize string to contain only ASCII digits (0-9)

## Usage

~~~~~
// basic usage
$string = $sanitizer->digits($value);

// usage with all arguments
$string = $sanitizer->digits($value, $maxLength = 1024);
~~~~~

## Arguments

- `$value` `string` Value to sanitize
- `$maxLength` (optional) `int` Maximum length of returned value (default=1024)

## Return value

- `string`
