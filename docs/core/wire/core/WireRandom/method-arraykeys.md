# $wireRandom->arrayKeys(array $a, $qty = 0): array

Source: `wire/core/WireRandom.php`

Get a random version of all keys in given array (or a specified quantity of them)

## Usage

~~~~~
// basic usage
$array = $wireRandom->arrayKeys($a);

// usage with all arguments
$array = $wireRandom->arrayKeys(array $a, $qty = 0);
~~~~~

## Arguments

- `$a` `array` Array to get random keys from.
- `$qty` (optional) `int` Quantity of unique keys to return or 0 for all (default=0)

## Return value

- `array`
