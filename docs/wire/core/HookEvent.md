# HookEvent

Source: `wire/core/HookEvent.php`

ProcessWire HookEvent

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

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

@property-read Wire|WireData|WireArray|Module $object Instance of the object where the Hook event originated.

@property-read string $method The name of the method that was called to generate the Hook event.

@property array $arguments A numerically indexed array of the arguments sent to the above mentioned method.

@property mixed $return Applicable only for 'after' or ('replace' + 'before' hooks), contains the value returned by the above mentioned method. The hook handling method may modify this return value.

@property bool $replace Set to boolean true in a 'before' hook if you want to prevent execution of the original hooked function. In such a case, your hook is replacing the function entirely. Not recommended, so be careful with this.

@property array $options An optional array of user-specified data that gets sent to the hooked function. The hook handling method may access it from $event->data. Also includes all the default hook properties.

@property-read string $id A unique identifier string that may be used with a call to `Wire::removeHook()`.

@property-read string $when In an active hook, contains either the string 'before' or 'after', indicating whether it is executing before or after the hooked method.

@property bool $cancelHooks When true, all remaining hooks will be cancelled, making this HookEvent the last one (be careful with this).

## __construct()

Construct the HookEvent and establish default values

@param array $eventData Optional event data to start with

## arguments()

Retrieve or set a hooked function argument

~~~~~
// Retrieve first argument by index (0=first)
$page = $event->arguments(0);

// Retrieve array of all arguments
$arguments = $event->arguments();

// Retrieve argument by name
$page = $event->arguments('page');

// Set first argument by index
$event->arguments(0, $page);

// Set first argument by name
$event->arguments('page', $page);
~~~~~

@param int $n Zero based number of the argument you want to retrieve, where 0 is the first.
	 May also be a string containing the argument name.
  Omit to return array of all arguments.

@param mixed $value Value that you want to set to this argument, or omit to only return the argument.

@return array|null|mixed

## argumentsByName()

Returns an array of all arguments indexed by name, or the value of a single specified argument

Note: `$event->arguments('name')` can also be used as a shorter synonym for `$event->argumentsByName('name')`.

~~~~~
// Get an array of all arguments indexed by name
$arguments = $event->argumentsByName();

// Get a specific argument by name
$page = $event->argumentsByName('page');
~~~~~

@param string $n Optional name of argument value to return. If not specified, array of all argument values returned.

@return mixed|array Depending on whether you specify $n

## getArgumentNames()

Return an array of all argument names, indexed by their position

@return array

## removeHook()

Remove a hook by ID

To remove the hook that this event is for, call it with the $hookId argument as null or blank.

~~~~~
// Remove this hook event, preventing it from executing again
$event->removeHook(null);
~~~~~

@param string|HookEvent|null $hookId

@return HookEvent|WireData $this

## get()

Get

@param object|string $key

@return mixed|null

## __toString()

Return a string representing the HookEvent
