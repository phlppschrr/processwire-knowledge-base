# $wireRandom->shuffle($value): string|array

Source: `wire/core/WireRandom.php`

Shuffle a string or an array

Unlike PHP’s shuffle() function, this method:

- Accepts strings or arrays and returns the same type.
- Maintains array keys, if given an array.
- Returns a copy of the value rather than modifying the given value directly.
- Is cryptographically secure if PHP7 or mcrypt available.

## Usage

~~~~~
// basic usage
$string = $wireRandom->shuffle($value);
~~~~~

## Arguments

- `$value` `string|array`

## Return value

- `string|array`
