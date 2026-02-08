# $wireHooks->isMethodHooked($class, $method): bool

Source: `wire/core/WireHooks.php`

Similar to isHooked() method but also checks parent classes for the hooked method as well

This method is designed for fast determinations of whether something is hooked

## Arguments

- string|Wire $class
- string $method Name of method

## Return value

bool
