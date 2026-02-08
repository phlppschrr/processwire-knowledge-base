# $wireInput->filterValue($value, array $valid, $getArray): array|string|null

Source: `wire/core/WireInput.php`

Filter value against given $valid whitelist

## Arguments

- string|array $value
- array $valid Whitelist of valid values
- bool $getArray Filter to allow multiple values (array)?

## Return value

array|string|null

## Throws

- WireException If given a multidimensional array for $valid argument
