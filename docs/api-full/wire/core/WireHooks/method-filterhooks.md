# $wireHooks->filterHooks(array $hooks, $property, $value): array

Source: `wire/core/WireHooks.php`

Filter and return hooks matching given property and value

## Usage

~~~~~
// basic usage
$array = $wireHooks->filterHooks($hooks, $property, $value);

// usage with all arguments
$array = $wireHooks->filterHooks(array $hooks, $property, $value);
~~~~~

## Arguments

- `$hooks` `array` Hooks from getHooks() method
- `$property` `string` Property name from hook (or hook options)
- `$value` `string|bool|int` Value to match

## Return value

- `array`
