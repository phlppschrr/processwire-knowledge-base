# $selector->__construct($field, $value)

Source: `wire/core/Selector.php`

Given a field name and value, construct the Selector.

If the provided $field is an array or pipe "|" separated string, Selector may match any of them (OR field condition)
If the provided $value is an array of pipe "|" separated string, Selector may match any one of them (OR value condition).

If only one field is provided as a string, and that field is prepended by an exclamation point, i.e. !field=something
then the condition is reversed.

## Arguments

- string|array $field
- string|int|array $value
