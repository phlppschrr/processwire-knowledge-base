# $sanitizer->options(array $values, array $allowedValues = array()): array

Source: `wire/core/Sanitizer.php`

Return given values that that also exist in $allowedValues whitelist

## Usage

~~~~~
// basic usage
$array = $sanitizer->options($values);

// usage with all arguments
$array = $sanitizer->options(array $values, array $allowedValues = array());
~~~~~

## Arguments

- `$values` `array`
- `$allowedValues` (optional) `array` Whitelist of option values that are allowed

## Return value

- `array`
