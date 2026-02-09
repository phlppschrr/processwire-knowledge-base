# HookEvent

Source: `wire/core/HookEvent.php`

Inherits: `WireData`

## Summary

ProcessWire HookEvent

Common methods:
- [`arguments()`](method-arguments.md)
- [`argumentsByName()`](method-argumentsbyname.md)
- [`setArgument()`](method-setargument.md)
- [`getArgumentNames()`](method-getargumentnames.md)
- [`removeHook()`](method-removehook.md)

Instances of HookEvent are passed to Hook handlers when their requested method has been called.

HookEvent is a type provided to hook functions with information about the event.
$event
~~~~~~
// Example
$wire->addHookAfter('Pages::saved', function(HookEvent $event) {
  $page = $event->arguments(0);
  $event->message("You saved page $page->path");
});
~~~~~~

HookEvents have the following properties available:

- `$object: Wire|WireData|WireArray|Module` Instance of the object where the Hook event originated.
- `$method: string` The name of the method that was called to generate the Hook event.
- [`$arguments: array`](method-arguments.md) A numerically indexed array of the arguments sent to the above mentioned method.
- `$return: mixed` Applicable only for 'after' or ('replace' + 'before' hooks), contains the value returned by the above mentioned method. The hook handling method may modify this return value.
- `$replace: bool` Set to boolean true in a 'before' hook if you want to prevent execution of the original hooked function. In such a case, your hook is replacing the function entirely. Not recommended, so be careful with this.
- `$options: array` An optional array of user-specified data that gets sent to the hooked function. The hook handling method may access it from $event->data. Also includes all the default hook properties.
- `$id: string` A unique identifier string that may be used with a call to `Wire::removeHook()`.
- `$when: string` In an active hook, contains either the string 'before' or 'after', indicating whether it is executing before or after the hooked method.
- `$cancelHooks: bool` When true, all remaining hooks will be cancelled, making this HookEvent the last one (be careful with this).

## Methods
- [`__construct(array $eventData = array())`](method-__construct.md) Construct the HookEvent and establish default values
- [`arguments(int $n = null, mixed $value = null): array|null|mixed`](method-arguments.md) Retrieve or set a hooked function argument
- [`argumentsByName(string $n = ''): mixed|array`](method-argumentsbyname.md) Returns an array of all arguments indexed by name, or the value of a single specified argument
- [`getArgumentNames(): array`](method-getargumentnames.md) Return an array of all argument names, indexed by their position
- [`removeHook(string|HookEvent|null $hookId): HookEvent|WireData`](method-removehook.md) Remove a hook by ID
- [`get(object|string $key): mixed|null`](method-get.md) Get
- [`__toString()`](method-__tostring.md) Return a string representing the HookEvent
