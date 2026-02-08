# Sanitizer::sanitize()

Source: `wire/core/Sanitizer.php`

Call a sanitizer method indirectly where method name can contain combined/combo methods

This method is primarily here to support predefined sanitizers in strings, like those that might
be specified in settings for a module or field. For regular use, you probably want to call the
sanitizer methods directly rather than through this method.

~~~~~
// sanitize with text then entities sanitizers
$value = $sanitizer->sanitize($value, 'text,entities');

// numbers appended to text sanitizers imply max length
$value = $sanitizer->sanitize($value, 'text128,entities');
~~~~~


@param mixed $value

@param string $method Method name "method", or combined method name(s) "method1,method2,method3"

@return string|int|array|float|null

@since 3.0.125
