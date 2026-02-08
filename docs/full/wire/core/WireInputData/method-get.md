# $wireInputData->get($key, $options = array()): string|int|float|array|null

Source: `wire/core/WireInputData.php`

Get a value

## Usage

~~~~~
// basic usage
$string = $wireInputData->get($key);

// usage with all arguments
$string = $wireInputData->get($key, $options = array());
~~~~~

## Arguments

- `$key` `string`
- `$options` (optional) `array|int|string` Options not currently used, but available for descending classes or future use

## Return value

- `string|int|float|array|null` $value

## Since

3.0.141 You can also get directly or use __get(), both of which are compatible with all versions
