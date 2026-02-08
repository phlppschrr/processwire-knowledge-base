# $functionsWireAPI->wireSanitizer($name = '', $value = ''): Sanitizer|string|int|array|null|mixed

Source: `wire/core/FunctionsWireAPI.php`

Access the $sanitizer API variable as a function

~~~~~
// Example usages
$clean = sanitizer()->pageName($dirty);
$clean = sanitizer('pageName', $dirty); // same as above
~~~~~

## Arguments

- string $name Optionally enter a sanitizer function name
- string $value If $name populated, enter the value to sanitize

## Return value

Sanitizer|string|int|array|null|mixed
