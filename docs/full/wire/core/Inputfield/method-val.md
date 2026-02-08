# $inputfield->val($value = null): string|int|float|array|object|Wire|WireData|WireArray|Inputfield

Source: `wire/core/Inputfield.php`

Shortcut for getting or setting “value” attribute

When setting a value, it returns $this (for fluent interface).

## Example

~~~~~
$value = $inputfield->val(); * // Getting
$inputfield->val('foo'); * // Setting
~~~~~

## Usage

~~~~~
// basic usage
$string = $inputfield->val();

// usage with all arguments
$string = $inputfield->val($value = null);
~~~~~

## Arguments

- `$value` (optional) `string|null`

## Return value

- `string|int|float|array|object|Wire|WireData|WireArray|Inputfield`
