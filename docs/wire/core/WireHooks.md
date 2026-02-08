# WireHooks

Source: `wire/core/WireHooks.php`

ProcessWire Hooks Manager

This class is for internal use. You should manipulate hooks from Wire-derived classes instead.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## ___debug

Debug hooks

## getHooksAll

Refers to ALL hooks

## getHooksLocal

Refers only to LOCAL hooks

## getHooksStatic

Refers only to STATIC hooks

## __construct()

Construct WireHooks

@param ProcessWire $wire

@param Config $config

## getHooks()

Return all hooks associated with $object or method (if specified)

@param Wire $object

@param string $method Optional method that hooks will be limited to. Or specify '*' to return all hooks everywhere.

@param int $getHooks Get hooks of type, specify one of the following constants:
	- WireHooks::getHooksAll returns all hooks [0] (default)
	- WireHooks::getHooksLocal returns local hooks [1] only
	- WireHooks::getHooksStatic returns static hooks [2] only

@return array

## isHooked()

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

## isHookedOrParents()

Similar to isHooked() method but also checks parent classes for the hooked method as well

This method is designed for fast determinations of whether something is hooked

@param string|Wire $class

@param string $method Name of method or property

@param string $type May be either 'method', 'property' or 'either'

@return bool

## isMethodHooked()

Similar to isHooked() method but also checks parent classes for the hooked method as well

This method is designed for fast determinations of whether something is hooked

@param string|Wire $class

@param string $method Name of method

@return bool

## isPropertyHooked()

Similar to isHooked() method but also checks parent classes for the hooked property as well

This method is designed for fast determinations of whether something is hooked

@param string|Wire $class

@param string $property Name of property

@return bool

## hasHook()

Similar to isHooked(), returns true if the method or property hooked, false if it isn't.

Accomplishes the same thing as the isHooked() method, but this is more accurate,
and potentially slower than isHooked(). Less for optimization use, more for accuracy use.

It checks for both static hooks and local hooks, but only accepts a method() or property
name as an argument (i.e. no Class::something) since the class context is assumed from the current
instance. Unlike isHooked() it also analyzes the instance's class parents for hooks, making it
more accurate. As a result, this method works well for more than just optimization use.

If checking for a hooked method, it should be in the form "method()".
If checking for a hooked property, it should be in the form "property".

@param Wire $object

@param string $method Method() or property name

@return bool

@throws WireException whe you try to call it with a Class::something() type method.

@todo differentiate between "method()" and "property"

## getClassParents()

Get an array of parent classes and interfaces for the given object

@param Wire|string $object Maybe either object instance or class name

@param bool $cache Allow use of cache for getting or storing? (default=true)

@return array

## addHook()

Hook a function/method to a hookable method call in this object

Hookable method calls are methods preceded by three underscores.
You may also specify a method that doesn't exist already in the class
The hook method that you define may be part of a class or a globally scoped function.

If you are hooking a procedural function, you may omit the $toObject and instead just call via:
$this->addHook($method, 'function_name'); or $this->addHook($method, 'function_name', $options);

@param Wire $object

@param string|array $method Method name to hook into, NOT including the three preceding underscores.
	May also be Class::Method for same result as using the fromClass option.
 May also be array OR CSV string of either of the above to add multiple (since 3.0.137).

@param object|null|callable $toObject Object to call $toMethod from,
	Or null if $toMethod is a function outside of an object,
	Or function|callable if $toObject is not applicable or function is provided as a closure.

@param string|array $toMethod Method from $toObject, or function name to call on a hook event, or $options array.

@param array $options See $defaultHookOptions at the beginning of this class. Optional.

@return string A special Hook ID that should be retained if you need to remove the hook later.
 If the $method argument was a CSV string or array of multiple methods to hook, then CSV string of hook IDs
 will be returned, and the same CSV string can be used with removeHook() calls. (since 3.0.137).

@throws WireException

## addHooks()

Add a hooks to multiple methods at once

This is the same as addHook() except that the $method argument is an array or CSV string of hook definitions.
See the addHook() method for more detailed info on arguments.

@param Wire $object

@param array|string $methods Array of one or more strings hook definitions, or CSV string of hook definitions

@param object|null|callable $toObject

@param string|array|null $toMethod

@param array $options

@return string CSV string of hook IDs that were added

@throws WireException

@since 3.0.137

## addPathHook()

Add a hook that handles a request path

@param Wire $object

@param string $path

@param Wire|null|callable $toObject

@param string $toMethod

@param array $options

@return string

@throws WireException

## runHooks()

Provides the implementation for calling hooks in ProcessWire

Unlike __call, this method won't trigger an Exception if the hook and method don't exist.
Instead it returns a result array containing information about the call.

@param Wire $object

@param string $method Method or property to run hooks for.

@param array $arguments Arguments passed to the method and hook.

@param string|array $type May be any one of the following:
 - method: for hooked methods (default)
 - property: for hooked properties
 - before: only run before hooks and do nothing else
 - after: only run after hooks and do nothing else
 - Or array[] of hooks (from getHooks method) to run (does not call hooked method)

@return array Returns an array with the following information:
	[return] => The value returned from the hook or NULL if no value returned or hook didn't exist.
	[numHooksRun] => The number of hooks that were actually run.
	[methodExists] => Did the hook method exist as a real method in the class? (i.e. with 3 underscores ___method).
	[replace] => Set by the hook at runtime if it wants to prevent execution of the original hooked method.

## prepareArgMatch()

Prepare argument match

@param string $argMatch

@return array

@since 3.0.247

## conditionalArgMatch()

Does given value match given match condition?

@param Selectors|string $argMatch

@param mixed $argVal

@return bool

@since 3.0.247

## allowRunPathHook()

Allow given path hook to run?

This checks if the hook’s path matches the request path, allowing for both
regular and regex matches and populating parenthesized portions to arguments
that will appear in the HookEvent.

@param string $id Hook ID

@param array $arguments

@return bool

@since 3.0.173

## filterHooks()

Filter and return hooks matching given property and value

@param array $hooks Hooks from getHooks() method

@param string $property Property name from hook (or hook options)

@param string|bool|int $value Value to match

@return array

## hookTimer()

Start timing a hook and return the timer name

@param Wire $object

@param String $method

@param array $arguments

@return string

## removeHook()

Given a Hook ID provided by addHook() this removes the hook

To have a hook function remove itself within the hook function, say this is your hook function:
function(HookEvent $event) {
  $event->removeHook(null); // remove self
}

@param Wire $object

@param string|array|null $hookID Can be single hook ID, array of hook IDs, or CSV string of hook IDs

@return Wire

## removeHooks()

Given a hook ID or multiple hook IDs (in array or CSV string) remove the hooks

@param Wire $object

@param array|string $hookIDs

@return Wire

@since 3.0.137

## getAllLocalHooks()

Return the "all local hooks" cache

@return array

## getAllPathHooks()

Return all pending path hooks

@return array

@since 3.0.173

## hasPathHooks()

Return whether or not any path hooks are pending

@param string $requestPath Optionally provide request path to determine if any might match (3.0.174+)

@return bool

@since 3.0.173

## filterPathHooks()

Return path hooks that have potential to match given request path

@param string $requestPath

@param bool $has Specify true to change return value to boolean as to whether any can match (default=false)

@return array|bool

@since 3.0.174

## allowPathHooks()

Get or set whether path hooks are allowed

@param bool|null $allow

@return bool

@since 3.0.173

## getPathHookRedirect()

Return redirect URL required by an applicable path hook, or blank otherwise

@return string

@since 3.0.173

## className()

@return string
