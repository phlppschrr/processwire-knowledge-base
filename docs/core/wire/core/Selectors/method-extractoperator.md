# $selectors->extractOperator(&$str, array $operatorChars): string

Source: `wire/core/Selectors.php`

Given a string starting with an operator, return that operator, and remove it from $str.

## Arguments

- `$str` `string`
- `$operatorChars` `array`

## Return value

string

## Deprecated

Replaced by extractOperators()

## Details

- @todo this method can be removed once confirmed nothing else uses it
