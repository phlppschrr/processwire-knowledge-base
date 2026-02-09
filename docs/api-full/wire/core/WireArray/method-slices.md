# $wireArray->slices($qty): array

Source: `wire/core/WireArray.php`

Divide this WireArray into $qty slices and return array of them (each being another WireArray)

This is not destructive to the original WireArray as it returns new WireArray objects.

## Usage

~~~~~
// basic usage
$array = $wireArray->slices($qty);
~~~~~

## Arguments

- `$qty` `int` Number of slices

## Return value

- `array` Array of WireArray objects
