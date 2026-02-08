# Fuel::set()

Source: `wire/core/Fuel.php`

@param string $key API variable name to set - should be valid PHP variable name.

@param object|mixed $value Value for the API variable.

@param bool $lock Whether to prevent this API variable from being overwritten in the future.

@return $this

@throws WireException When you try to set a previously locked API variable, a WireException will be thrown.
