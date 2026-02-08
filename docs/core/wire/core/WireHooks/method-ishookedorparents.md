# $wireHooks->isHookedOrParents($class, $method, $type = 'either'): bool

Source: `wire/core/WireHooks.php`

Similar to isHooked() method but also checks parent classes for the hooked method as well

This method is designed for fast determinations of whether something is hooked

## Arguments

- `$class` `string|Wire`
- `$method` `string` Name of method or property
- `$type` (optional) `string` May be either 'method', 'property' or 'either'

## Return value

bool
