# $wireArray->__get($name): Wire|WireData|Page|mixed|bool

Source: `wire/core/WireArray.php`

Enables derefencing of WireArray elements in object notation.

Example: $myArray->myElement
Not applicable to numerically indexed arrays.
Fuel properties and hooked properties have precedence with this type of call.

## Arguments

- int|string $name

## Return value

Wire|WireData|Page|mixed|bool Value of item requested, or false if it doesn't exist.
