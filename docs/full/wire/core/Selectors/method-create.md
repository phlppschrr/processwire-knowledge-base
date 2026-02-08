# $selectors->create($field, $operator, $value): Selector

Source: `wire/core/Selectors.php`

Create a new Selector object from a field name, operator, and value

This is mostly for internal use, as the Selectors object already does this when you pass it
a selector string in the constructor or init() method.

## Arguments

- string $field Field name or names (separated by a pipe)
- string $operator Operator, i.e. "="
- string|array $value Value or values (separated by a pipe)

## Return value

Selector Returns the correct type of `Selector` object that corresponds to the given `$operator`.

## Throws

- WireException
