# $wireHooks->allowRunPathHook($id, array &$arguments): bool

Source: `wire/core/WireHooks.php`

Allow given path hook to run?

This checks if the hook’s path matches the request path, allowing for both
regular and regex matches and populating parenthesized portions to arguments
that will appear in the HookEvent.

## Usage

~~~~~
// basic usage
$bool = $wireHooks->allowRunPathHook($id, $arguments);

// usage with all arguments
$bool = $wireHooks->allowRunPathHook($id, array &$arguments);
~~~~~

## Arguments

- `$id` `string` Hook ID
- `$arguments` `array`

## Return value

- `bool`

## Since

3.0.173
