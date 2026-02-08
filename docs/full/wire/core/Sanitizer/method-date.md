# $sanitizer->date($value, $format = null, array $options = array()): string|int|null

Source: `wire/core/Sanitizer.php`

Sanitize a date or date/time string, making sure it is valid, and return it

- If no date $format is specified, date will be returned as a unix timestamp.
- If given date in invalid format and can’t be made valid, or date is empty, NULL will be returned.
- If $value is an integer or string of all numbers, it is always assumed to be a unix timestamp.
- If $format and “strict” option specified, date will also validate for format and no out-of-bounds values will be converted.

## Arguments

- string|int $value Date string or unix timestamp
- string|null $format Format of date string ($value) in any wireDate(), date() or strftime() format.
- array $options Options to modify behavior: - `returnFormat` (string): wireDate() format to return date in. If not specified, then the $format argument is used. - `min` (string|int): Minimum allowed date in $format or unix timestamp format. Null is returned when date is less than this. - `max` (string|int): Maximum allowed date in $format or unix timestamp format. Null is returned when date is more than this. - `default` (mixed): Default value to return if no value specified. - `strict` (bool): Force dates that don’t match given $format, or out of bounds, to fail. Requires $format. (default=false)

## Return value

string|int|null
