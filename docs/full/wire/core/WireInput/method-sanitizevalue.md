# WireInput::sanitizeValue()

Source: `wire/core/WireInput.php`

Sanitize the given value with the given method(s)

@param string $method Sanitizer method name or CSV string of sanitizer method names

@param string|array|null $value

@param bool $getArray

@return array|int|float|string|null

@throws WireException If given unknown sanitizer method
