# WireInput::filterValue()

Source: `wire/core/WireInput.php`

Filter value against given $valid whitelist

@param string|array $value

@param array $valid Whitelist of valid values

@param bool $getArray Filter to allow multiple values (array)?

@return array|string|null

@throws WireException If given a multidimensional array for $valid argument
