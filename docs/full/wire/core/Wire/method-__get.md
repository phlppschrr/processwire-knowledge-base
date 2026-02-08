# Wire::__get()

Source: `wire/core/Wire.php`

Get an object property by direct reference or NULL if it doesn't exist

If not overridden, this is primarily used as a shortcut for the fuel() method.

Descending classes may have their own __get() but must pass control to this one when they can't find something.

@param string $name

@return mixed|null
