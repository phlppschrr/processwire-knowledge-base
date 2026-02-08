# $functionsAPI->sanitizer($name = '', $value = ''): Sanitizer|string|int|array|null|mixed

Source: `wire/core/FunctionsAPI.php`

Sanitize variables and related string functions ($sanitizer API variable as a function)

This behaves the same as the `$sanitizer` API variable but supports arguments as optional shortcuts.

~~~~~
$clean = sanitizer()->pageName($dirty); // regular syntax
$clean = sanitizer('pageName', $dirty); // shortcut syntax
~~~~~

## Arguments

- string $name Optionally enter a sanitizer function name
- string $value If $name populated, enter the value to sanitize

## Return value

Sanitizer|string|int|array|null|mixed

## See also

- Sanitizer
