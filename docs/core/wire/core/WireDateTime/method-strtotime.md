# WireDateTime::strtotime()

Source: `wire/core/WireDateTime.php`

Parse about any English textual datetime description into a Unix timestamp using PHP’s strtotime()

This function behaves the same as PHP’s version except that it optionally accepts an `$options` array
and lets you specify the return value for empty or zeroed dates like 0000-00-00. If given a zero’d date
then it returns null by default (rather than throwing an error as PHP8 does). As of 3.0.238+ this method
also lets you optionally specify an input format should the given date string not be strtotime compatible.

@param string $str Date/time string

@param array|int $options Options to modify behavior, or specify int for the `baseTimestamp` option, or string for `inputFormat` option.
 - `emptyReturnValue` (int|null|false): Value to return for empty or zero-only date strings (default=null)
 - `baseTimestamp` (int|null): The timestamp which is used as a base for the calculation of relative dates.
 - `inputFormat` (string): Optional date format that given $str is in, if not strtotime() compatible. (3.0.238+)
 - `outputFormat` (string): Optionally return value in this date format rather than unix timestamp (3.0.238+)

@return false|int|null

@see https://www.php.net/manual/en/function.strtotime.php

@since 3.0.178
