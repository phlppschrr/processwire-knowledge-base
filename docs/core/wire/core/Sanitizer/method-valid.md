# Sanitizer::valid()

Source: `wire/core/Sanitizer.php`

Is given value valid? (i.e. unchanged by given sanitizer method)

~~~~~~
if($sanitizer->valid('abc123', 'alphanumeric')) {
 // value is valid
}
~~~~~~


@param string|int|array|float $value Value to check if valid

@param string $method Method name or CSV method names

@param bool $strict When true, sanitized value must be identical in type to the one given

@return bool

@since 3.0.125
