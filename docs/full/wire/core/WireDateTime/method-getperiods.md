# $wireDateTime->getPeriods($abbreviate, $plural = null): array

Source: `wire/core/WireDateTime.php`

Get named time periods

Returns regular array(s) of periods in this order:
seconds, minutes, hours, days, weeks, months, years decades

If $plural argument is null (or omitted) it instead returns an array
indexed by period name including both singular and plural periods.

## Arguments

- $abbreviate - Specify 1 to get shortest possible abbreviations - Specify true to get standard/medium abbreviations - Specify false to get large/full terms (no abbreviations) - Specify associative array to get large/full terms and substitute your own
- `$plural` (optional) `null|true|int` - Specify true to get plural, - Specify false to get singular, - Specify 1 to get array where [ 0 => [singulars], 1 => [plurals] ] - Omit (or null) to get all in an indexed array

## Return value

array
