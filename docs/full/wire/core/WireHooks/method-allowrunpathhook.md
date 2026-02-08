# $wireHooks->allowRunPathHook($id, array &$arguments): bool

Source: `wire/core/WireHooks.php`

Allow given path hook to run?

This checks if the hook’s path matches the request path, allowing for both
regular and regex matches and populating parenthesized portions to arguments
that will appear in the HookEvent.

## Arguments

- string $id Hook ID
- array $arguments

## Return value

bool

## Meta

- @since 3.0.173
