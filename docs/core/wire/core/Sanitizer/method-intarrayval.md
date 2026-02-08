# $sanitizer->intArrayVal($value, $options = array()): array

Source: `wire/core/Sanitizer.php`

Sanitize array to be all unsigned integers with no conversions

This is the same as the `intArray()` method except for the following:

 - The `csv` delimited string conversion option is disabled by default.
 - The `strict` option default is true, meaning non-integer numbers or those outside allowed range
   are removed rather than converted.

## Arguments

- `$value` `array|string|mixed` Accepts an array or CSV string. If given something else, it becomes first value in array.
- `$options` (optional) `array|bool` Options to modify behavior or specify bool for `strict` option: - `min` (int): Minimum allowed value (default=0) - `max` (int): Maximum allowed value (default=PHP_INT_MAX) - `maxItems` (int): Maximum items allowed in each array (default=0, which means no limit) - `maxDepth` (int): Max nested array depth (default=0, which means no nesting allowed) Since 3.0.160 - `strict` (bool): Remove rather than convert any values that are not all digits or fall outside min/max range? (default=true) Note that this default for the strict option is different from the one on the intArray() method.

## Return value

array Array of integers

## Since

3.0.165
