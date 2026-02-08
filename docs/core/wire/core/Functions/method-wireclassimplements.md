# Functions::wireClassImplements()

Source: `wire/core/Functions.php`

Get an array of all the interfaces that the given class implements

- ProcessWire namespace aware version of PHP’s class_implements() function.
- Return value has array keys as class name with namespace and array values as class name without namespace.


@param string|object $className

@param bool $autoload

@return array
