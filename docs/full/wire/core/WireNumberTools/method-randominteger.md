# $wireNumberTools->randomInteger($min, $max, $throw = false): int

Source: `wire/core/WireNumberTools.php`

Return a random integer (cryptographically secure when available)

## Usage

~~~~~
// basic usage
$int = $wireNumberTools->randomInteger($min, $max);

// usage with all arguments
$int = $wireNumberTools->randomInteger($min, $max, $throw = false);
~~~~~

## Arguments

- `$min` `int` Minimum value (default=0)
- `$max` `int` Maximum value (default=PHP_INT_MAX)
- `$throw` (optional) `bool` Throw WireException if we cannot achieve a cryptographically secure random number? (default=false)

## Return value

- `int`

## Since

3.0.214
