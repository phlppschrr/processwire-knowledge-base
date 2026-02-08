# WireHooks::isHooked()

Source: `wire/core/WireHooks.php`

Returns true if the method/property hooked, false if it isn't.

This is for optimization use. It does not distinguish about class instance.
It only distinguishes about class if you provide a class with the $method argument (i.e. Class::).
As a result, a true return value indicates something "might" be hooked, as opposed to be
being definitely hooked.

If checking for a hooked method, it should be in the form `Class::method()` or `method()` (with parenthesis).
If checking for a hooked property, it should be in the form `Class::property` or `property`.

If you need to check if a method/property is hooked, including any of its parent classes, use
the `WireHooks::isMethodHooked()`, `WireHooks::isPropertyHooked()`, or `WireHooks::hasHook()` methods instead.

@param string $method Method or property name in one of the following formats:
	Class::method()
	Class::property
	method()
	property

@param Wire|null $instance Optional instance to check against (see hasHook method for details)
	Note that if specifying an $instance, you may not use the Class::method() or Class::property options for $method argument.

@return bool

@see WireHooks::isMethodHooked(), WireHooks::isPropertyHooked(), WireHooks::hasHook()
