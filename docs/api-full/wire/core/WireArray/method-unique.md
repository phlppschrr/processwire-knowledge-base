# $wireArray->unique($sortFlags = SORT_STRING): WireArray

Source: `wire/core/WireArray.php`

Return a new array that is unique (no two of the same elements)

This is the equivalent to PHP's [array_unique()](http://php.net/manual/en/function.array-unique.php) function.

## Usage

~~~~~
// basic usage
$items = $wireArray->unique();

// usage with all arguments
$items = $wireArray->unique($sortFlags = SORT_STRING);
~~~~~

## Arguments

- `$sortFlags` (optional) `int` Sort flags per PHP's `array_unique()` function (default=`SORT_STRING`)

## Return value

- `WireArray`
