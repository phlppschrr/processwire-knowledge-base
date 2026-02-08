# FunctionsWireAPI::wireSanitizer()

Source: `wire/core/FunctionsWireAPI.php`

Access the $sanitizer API variable as a function

~~~~~
// Example usages
$clean = sanitizer()->pageName($dirty);
$clean = sanitizer('pageName', $dirty); // same as above
~~~~~

@param string $name Optionally enter a sanitizer function name

@param string $value If $name populated, enter the value to sanitize

@return Sanitizer|string|int|array|null|mixed
