# $functions->wireBytesStr($bytes, $small = false, $options = array()): string

Source: `wire/core/Functions.php`

Given a quantity of bytes (int), return readable string that refers to quantity in bytes, kB, MB, GB and TB

## Arguments

- `$bytes` `int` Quantity in bytes
- `$small` (optional) `bool|int|array` Make returned string as small as possible? (default=false) - `true` (bool): Yes, make returned string as small as possible. - `1` (int): Same as `true` but with space between number and unit label. - Or optionally specify the $options argument here if you do not need the $small argument.
- `$options` (optional) `array|int` Options to modify default behavior, or if an integer then `decimals` option is assumed: - `decimals` (int|null): Number of decimals to use in returned value or NULL for auto (default=null). When null (auto) a decimal value of 1 is used when appropriate, for megabytes and higher (3.0.214+). - `decimal_point` (string|null): Decimal point character, or null to detect from locale (default=null). - `thousands_sep` (string|null): Thousands separator, or null to detect from locale (default=null). - `small` (bool): If no $small argument was specified, you can optionally specify it in this $options array. - `type` (string): To force return value as specific type, specify one of: bytes, kilobytes, megabytes, gigabytes, terabytes; or just: b, k, m, g, t. (3.0.148+ only, terabytes 3.0.214+).

## Return value

string
