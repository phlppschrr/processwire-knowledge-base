# $functionsAPI->sanitizer($name = '', $value = ''): Sanitizer|string|int|array|null|mixed

Source: `wire/core/FunctionsAPI.php`

Sanitize variables and related string functions ($sanitizer API variable as a function)

This behaves the same as the `$sanitizer` API variable but supports arguments as optional shortcuts.

~~~~~
$clean = sanitizer()->pageName($dirty); // regular syntax
$clean = sanitizer('pageName', $dirty); // shortcut syntax
~~~~~

## Arguments

- `$name` (optional) `string` Optionally enter a sanitizer function name
- `$value` (optional) `string` If $name populated, enter the value to sanitize

## Return value

Sanitizer|string|int|array|null|mixed

## See also

- Sanitizer
