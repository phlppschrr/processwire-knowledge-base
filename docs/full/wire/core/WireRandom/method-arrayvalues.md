# $wireRandom->arrayValues(array $a, $qty = 0): array

Source: `wire/core/WireRandom.php`

Return a random version of given array or a quantity of random items

Array keys are retained in return value, unless requested $qty exceeds
the quantity of items in given array.

## Usage

~~~~~
// basic usage
$array = $wireRandom->arrayValues($a);

// usage with all arguments
$array = $wireRandom->arrayValues(array $a, $qty = 0);
~~~~~

## Arguments

- `$a` `array` Array to get random items from.
- `$qty` (optional) `int` Quantity of items, or 0 to return all (default=0).

## Return value

- `array`
