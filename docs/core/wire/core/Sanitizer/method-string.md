# Sanitizer::string()

Source: `wire/core/Sanitizer.php`

Sanitize value to string

Note that this makes no assumptions about what is a "safe" string, so you should always apply another
sanitizer to it.


@param string|int|array|object|bool|float $value Value to sanitize as string

@param string|null Optional sanitizer method (from this class) to apply to the string before returning

@return string
