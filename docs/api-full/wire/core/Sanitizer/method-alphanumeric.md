# $sanitizer->alphanumeric($value, $beautify = false, $maxLength = 1024): string

Source: `wire/core/Sanitizer.php`

Sanitize to ASCII alphanumeric (a-z A-Z 0-9)

## Usage

~~~~~
// basic usage
$string = $sanitizer->alphanumeric($value);

// usage with all arguments
$string = $sanitizer->alphanumeric($value, $beautify = false, $maxLength = 1024);
~~~~~

## Arguments

- `$value` `string` Value to sanitize
- `$beautify` (optional) `bool|int` Whether to beautify (See Sanitizer::translate option too)
- `$maxLength` (optional) `int` Maximum length of returned value (default=1024)

## Return value

- `string`
