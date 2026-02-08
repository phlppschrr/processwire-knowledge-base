# $sanitizer->arrayVal($value, $options = array()): array

Source: `wire/core/Sanitizer.php`

Simply sanitize value to array with no conversions

This is the same as the `array()` sanitizer except that it does not attempt to convert
delimited/csv strings to arrays. Meaning, a delimited string would simply become an array
with the first item being that delimited string.

## Arguments

- `$value` `mixed`
- `$options` (optional) `array` - `maxItems` (int): Maximum items allowed in each array (default=0, which means no limit) - `maxDepth` (int): Max nested array depth (default=0, which means no nesting allowed) - `sanitizer` (string): Optionally specify sanitizer method name to apply to items (default='') - `keySanitizer` (string): Optionally sanitize associative array keys with this method (default='') Since 3.0.167

## Return value

array

## Throws

- WireException

## Since

3.0.165
