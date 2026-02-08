# Selectors::create()

Source: `wire/core/Selectors.php`

Create a new Selector object from a field name, operator, and value

This is mostly for internal use, as the Selectors object already does this when you pass it
a selector string in the constructor or init() method.


@param string $field Field name or names (separated by a pipe)

@param string $operator Operator, i.e. "="

@param string|array $value Value or values (separated by a pipe)

@return Selector Returns the correct type of `Selector` object that corresponds to the given `$operator`.

@throws WireException
