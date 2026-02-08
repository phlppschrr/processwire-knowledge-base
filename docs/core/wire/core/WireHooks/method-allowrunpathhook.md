# WireHooks::allowRunPathHook()

Source: `wire/core/WireHooks.php`

Allow given path hook to run?

This checks if the hook’s path matches the request path, allowing for both
regular and regex matches and populating parenthesized portions to arguments
that will appear in the HookEvent.

@param string $id Hook ID

@param array $arguments

@return bool

@since 3.0.173
