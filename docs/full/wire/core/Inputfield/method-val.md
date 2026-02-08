# $inputfield->val($value = null): string|int|float|array|object|Wire|WireData|WireArray|Inputfield

Source: `wire/core/Inputfield.php`

Shortcut for getting or setting “value” attribute

When setting a value, it returns $this (for fluent interface).

~~~~~
$value = $inputfield->val(); * // Getting
$inputfield->val('foo'); * // Setting
~~~~~

## Arguments

- string|null $value

## Return value

string|int|float|array|object|Wire|WireData|WireArray|Inputfield
