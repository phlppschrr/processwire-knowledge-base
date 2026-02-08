# WireHooks::runHooks()

Source: `wire/core/WireHooks.php`

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
