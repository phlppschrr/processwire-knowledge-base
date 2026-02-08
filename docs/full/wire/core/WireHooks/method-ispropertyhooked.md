# $wireHooks->isPropertyHooked($class, $property): bool

Source: `wire/core/WireHooks.php`

Similar to isHooked() method but also checks parent classes for the hooked property as well

This method is designed for fast determinations of whether something is hooked

## Arguments

- string|Wire $class
- string $property Name of property

## Return value

bool
