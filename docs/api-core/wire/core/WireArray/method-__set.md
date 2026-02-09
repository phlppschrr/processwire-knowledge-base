# $wireArray->__set($property, $value)

Source: `wire/core/WireArray.php`

Enables setting of WireArray elements in object notation.

Example: $myArray->myElement = 10;
Not applicable to numerically indexed arrays.

## Usage

~~~~~
// basic usage
$result = $wireArray->__set($property, $value);
~~~~~

## Arguments

- `$property` `int|string` Key of item to set.
- int|string|array|object Value of item to set.

## Exceptions

- `WireException`
