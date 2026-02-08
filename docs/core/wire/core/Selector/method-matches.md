# $selector->matches($value): bool

Source: `wire/core/Selector.php`

Does this Selector match the given value?

If the value held by this Selector is an array of values, it will check if any one of them matches the value supplied here.

## Arguments

- string|int|Wire|array $value If given a Wire, then matches will also operate on OR field=value type selectors, where present

## Return value

bool
