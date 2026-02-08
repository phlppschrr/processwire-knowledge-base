# $inputfieldWrapper->getValueByName($name): array|float|int|object|Wire|WireArray|WireData|string|null

Source: `wire/core/InputfieldWrapper.php`

Get value of Inputfield by name

This traverses all children recursively to find the requested Inputfield,
and get the value attribute from it. A value of null is returned if the
Inputfield cannot be found.

## Usage

~~~~~
// basic usage
$array = $inputfieldWrapper->getValueByName($name);
~~~~~

## Arguments

- `$name` `string`

## Return value

- `array|float|int|object|Wire|WireArray|WireData|string|null`

## Since

3.0.172
