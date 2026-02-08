# $wireHooks->hasHook(Wire $object, $method): bool

Source: `wire/core/WireHooks.php`

Similar to isHooked(), returns true if the method or property hooked, false if it isn't.

Accomplishes the same thing as the isHooked() method, but this is more accurate,
and potentially slower than isHooked(). Less for optimization use, more for accuracy use.

It checks for both static hooks and local hooks, but only accepts a method() or property
name as an argument (i.e. no Class::something) since the class context is assumed from the current
instance. Unlike isHooked() it also analyzes the instance's class parents for hooks, making it
more accurate. As a result, this method works well for more than just optimization use.

If checking for a hooked method, it should be in the form "method()".
If checking for a hooked property, it should be in the form "property".

## Arguments

- Wire $object
- string $method Method() or property name

## Return value

bool

## Throws

- WireException whe you try to call it with a Class::something() type method.

## Meta

- @todo differentiate between "method()" and "property"
