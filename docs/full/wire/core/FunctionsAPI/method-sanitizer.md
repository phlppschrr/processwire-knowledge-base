# FunctionsAPI::sanitizer()

Source: `wire/core/FunctionsAPI.php`

Sanitize variables and related string functions ($sanitizer API variable as a function)

This behaves the same as the `$sanitizer` API variable but supports arguments as optional shortcuts.

~~~~~
$clean = sanitizer()->pageName($dirty); // regular syntax
$clean = sanitizer('pageName', $dirty); // shortcut syntax
~~~~~


@param string $name Optionally enter a sanitizer function name

@param string $value If $name populated, enter the value to sanitize

@return Sanitizer|string|int|array|null|mixed

@see Sanitizer
