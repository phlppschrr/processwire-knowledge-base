# $sanitizer->intArray($value, $options = array()): array

Source: `wire/core/Sanitizer.php`

Sanitize array or CSV string to array of unsigned integers (or signed integers if specified $min is less than 0)

If string specified, string delimiter may be comma (","), or pipe ("|"), or you may override with the 'delimiter' option.

## Arguments

- array|string|mixed $value Accepts an array or CSV string. If given something else, it becomes first value in array.
- array|bool $options Optional options (see `Sanitizer::array()` and `Sanitizer::int()` methods for options), plus these two: - `min` (int): Minimum allowed value (default=0) - `max` (int): Maximum allowed value (default=PHP_INT_MAX) - `strict` (bool): Remove rather than convert any values that are not all digits or fall outside min/max range? (default=false) Since 3.0.157+ - `maxItems` (int): Maximum items allowed in each array (default=0, which means no limit) - `maxDepth` (int): Max nested array depth (default=0, which means no nesting allowed) Since 3.0.160 - You may specify boolean true for $options argument to use just the `strict` option. (3.0.157+) - The following options are only used if the provided $value is a string: - `csv` (bool): Allow conversion of delimited string to array? (default=true) Since 3.0.165 - `delimiter` (string): Single delimiter to use to identify CSV strings. Overrides the 'delimiters' option when specified (default=null) - `delimiters` (array): Delimiters to identify CSV strings. First found delimiter will be used, default=array("|", ",") - `enclosure` (string): Enclosure to use for CSV strings (default=double quote, i.e. `"`)

## Return value

array Array of integers
