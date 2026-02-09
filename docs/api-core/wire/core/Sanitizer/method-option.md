# $sanitizer->option($value, array $allowedValues = array()): string|int|null

Source: `wire/core/Sanitizer.php`

Return $value if it exists in $allowedValues, or null if it doesn't

## Usage

~~~~~
// basic usage
$string = $sanitizer->option($value);

// usage with all arguments
$string = $sanitizer->option($value, array $allowedValues = array());
~~~~~

## Arguments

- `$value` `string|int`
- `$allowedValues` (optional) `array` Whitelist of option values that are allowed

## Return value

- `string|int|null`
