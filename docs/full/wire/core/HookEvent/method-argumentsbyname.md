# $hookEvent->argumentsByName($n = ''): mixed|array

Source: `wire/core/HookEvent.php`

Returns an array of all arguments indexed by name, or the value of a single specified argument

Note: `$event->arguments('name')` can also be used as a shorter synonym for `$event->argumentsByName('name')`.

~~~~~
// Get an array of all arguments indexed by name
$arguments = $event->argumentsByName();

// Get a specific argument by name
$page = $event->argumentsByName('page');
~~~~~

## Arguments

- string $n Optional name of argument value to return. If not specified, array of all argument values returned.

## Return value

mixed|array Depending on whether you specify $n
