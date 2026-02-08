# Sanitizer::selectorValueV2()

Source: `wire/core/Sanitizer.php`

Sanitize selector value (version 2, 3.0.156+)

This version is a little more thorough and has more options than version 1.

@param string|array $value

@param array $options

@return bool|mixed|string Always returns string unless you specify something different for 'emptyValue'
