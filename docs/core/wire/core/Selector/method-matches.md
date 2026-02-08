# Selector::matches()

Source: `wire/core/Selector.php`

Does this Selector match the given value?

If the value held by this Selector is an array of values, it will check if any one of them matches the value supplied here.

@param string|int|Wire|array $value If given a Wire, then matches will also operate on OR field=value type selectors, where present

@return bool
