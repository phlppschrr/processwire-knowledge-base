# WireHooks::isHookedOrParents()

Source: `wire/core/WireHooks.php`

Similar to isHooked() method but also checks parent classes for the hooked method as well

This method is designed for fast determinations of whether something is hooked

@param string|Wire $class

@param string $method Name of method or property

@param string $type May be either 'method', 'property' or 'either'

@return bool
