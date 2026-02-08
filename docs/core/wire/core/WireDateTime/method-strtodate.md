# WireDateTime::strtodate()

Source: `wire/core/WireDateTime.php`

Parse English textual datetime description into a formatted date string, or blank if not a date

@param string $str Date/time string to parse

@param string|array $format Output format to use, or array for $options.
 - Omit or boolean true for default 'Y-m-d H:i:s'.
 - Specify date format string, see [formats](https://www.php.net/manual/en/datetime.format.php).
 - Specify boolean false for unix timestamp.
 - Specify array of options.

@param array $options Can also be specified as 2nd argument. Options include:
 - `emptyReturnValue` (int|null|false): Value to return for empty or zero-only date strings (default='')
 - `baseTimestamp` (int|null): The timestamp which is used as a base for the calculation of relative dates.
 - `inputFormat` (string): Optional date format that given $str is in, if not strtotime() compatible.
 - `outputFormat` (string|bool): Format to return date string in, used only if $options specified for $format argument.
 - `format` (string|bool) Optional alias of outputFormat, used only if $options specified for $format argument.

@return string Return string, returns blank string on fail.

@since 3.0.238
