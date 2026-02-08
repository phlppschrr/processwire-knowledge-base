# $wireHooks->allowRunPathHook($id, array &$arguments): bool

Source: `wire/core/WireHooks.php`

Allow given path hook to run?

This checks if the hook’s path matches the request path, allowing for both
regular and regex matches and populating parenthesized portions to arguments
that will appear in the HookEvent.

## Arguments

- `$id` `string` Hook ID
- `$arguments` `array`

## Return value

bool

## Since

3.0.173
