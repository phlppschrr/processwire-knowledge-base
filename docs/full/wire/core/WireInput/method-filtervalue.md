# $wireInput->filterValue($value, array $valid, $getArray): array|string|null

Source: `wire/core/WireInput.php`

Filter value against given $valid whitelist

## Usage

~~~~~
// basic usage
$array = $wireInput->filterValue($value, $valid, $getArray);

// usage with all arguments
$array = $wireInput->filterValue($value, array $valid, $getArray);
~~~~~

## Arguments

- `$value` `string|array`
- `$valid` `array` Whitelist of valid values
- `$getArray` `bool` Filter to allow multiple values (array)?

## Return value

- `array|string|null`

## Exceptions

- `WireException` If given a multidimensional array for $valid argument
