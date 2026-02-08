# $wireInput->filterValue($value, array $valid, $getArray): array|string|null

Source: `wire/core/WireInput.php`

Filter value against given $valid whitelist

## Arguments

- `$value` `string|array`
- `$valid` `array` Whitelist of valid values
- `$getArray` `bool` Filter to allow multiple values (array)?

## Return value

array|string|null

## Throws

- WireException If given a multidimensional array for $valid argument
