# $functions->wireCount($value): int

Source: `wire/core/Functions.php`

Return the count of item(s) present in the given value

Duplicates behavior of PHP count() function prior to PHP 7.2, which states:

> Returns the number of elements in $value. When the parameter is neither an array nor an
object with implemented Countable interface, 1 will be returned. There is one exception,
if $value is NULL, 0 will be returned.

## Usage

~~~~~
// basic usage
$int = $functions->wireCount($value);
~~~~~

## Arguments

- `$value` `mixed`

## Return value

- `int`
