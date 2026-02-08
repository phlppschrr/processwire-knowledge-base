# $selectors->extractOperator(&$str, array $operatorChars): string

Source: `wire/core/Selectors.php`

Given a string starting with an operator, return that operator, and remove it from $str.

## Arguments

- string $str
- array $operatorChars

## Return value

string

## Meta

- @deprecated Replaced by extractOperators()
- @todo this method can be removed once confirmed nothing else uses it
