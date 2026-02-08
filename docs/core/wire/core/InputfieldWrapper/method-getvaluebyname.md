# $inputfieldWrapper->getValueByName($name): array|float|int|object|Wire|WireArray|WireData|string|null

Source: `wire/core/InputfieldWrapper.php`

Get value of Inputfield by name

This traverses all children recursively to find the requested Inputfield,
and get the value attribute from it. A value of null is returned if the
Inputfield cannot be found.

## Arguments

- string $name

## Return value

array|float|int|object|Wire|WireArray|WireData|string|null

## Meta

- @since 3.0.172
