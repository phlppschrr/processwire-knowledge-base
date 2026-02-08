# WireHooks::addHook()

Source: `wire/core/WireHooks.php`

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
