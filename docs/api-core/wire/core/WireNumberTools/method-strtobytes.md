# $wireNumberTools->strToBytes($value, $unit = null): int

Source: `wire/core/WireNumberTools.php`

Given a value like "1M", "2MB", "3 kB", "4 GB", "5tb" etc. return quantity of bytes

Spaces, commas and case in given value do not matter. Only the first character of the unit is
taken into account, whether it appears in the given value, or is given in the $unit argument.
Meaning a unit like megabytes (for example) can be specified as 'm', 'mb', 'megabytes', etc.

## Usage

~~~~~
// basic usage
$int = $wireNumberTools->strToBytes($value);

// usage with all arguments
$int = $wireNumberTools->strToBytes($value, $unit = null);
~~~~~

## Arguments

- `$value` `string|int|float`
- `$unit` (optional) `string|null` Optional unit that given value is in (b, kb, mb, gb, tb), or omit to auto-detect

## Return value

- `int`

## Since

3.0.214
