# $wireHooks->isMethodHooked($class, $method): bool

Source: `wire/core/WireHooks.php`

Similar to isHooked() method but also checks parent classes for the hooked method as well

This method is designed for fast determinations of whether something is hooked

## Usage

~~~~~
// basic usage
$bool = $wireHooks->isMethodHooked($class, $method);
~~~~~

## Arguments

- `$class` `string|Wire`
- `$method` `string` Name of method

## Return value

- `bool`
