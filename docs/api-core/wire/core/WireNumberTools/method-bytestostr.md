# $wireNumberTools->bytesToStr($bytes, $options = array()): string

Source: `wire/core/WireNumberTools.php`

Given a quantity of bytes (int), return readable string that refers to quantity in bytes, kB, MB, GB and TB

## Usage

~~~~~
// basic usage
$string = $wireNumberTools->bytesToStr($bytes);

// usage with all arguments
$string = $wireNumberTools->bytesToStr($bytes, $options = array());
~~~~~

## Arguments

- `$bytes` `int|string` Quantity in bytes (int) or any string accepted by strToBytes method.
- `$options` (optional) `array|int` Options to modify default behavior, or if an integer then `decimals` option is assumed: - `decimals` (int|null): Number of decimals to use in returned value or NULL for auto (default=null). When null (auto) a decimal value of 1 is used when appropriate, for megabytes and higher (3.0.214+). - `decimal_point` (string|null): Decimal point character, or null to detect from locale (default=null). - `thousands_sep` (string|null): Thousands separator, or null to detect from locale (default=null). - `small` (bool|int): Make returned string as small as possible? false=no, true=yes, 1=yes with space (default=false) - `labels` (array): Labels to use for units, indexed by: b, byte, bytes, k, m, g, t - `type` (string): To force return value as specific type, specify one of: bytes, kilobytes, megabytes, gigabytes, terabytes; or just: b, k, m, g, t. (3.0.148+ only, terabytes 3.0.214+).

## Return value

- `string`

## Since

3.0.214 All versions can also use the wireBytesStr() function
