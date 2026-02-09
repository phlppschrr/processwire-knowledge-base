# $functionsWireAPI->wireSanitizer($name = '', $value = ''): Sanitizer|string|int|array|null|mixed

Source: `wire/core/FunctionsWireAPI.php`

Access the $sanitizer API variable as a function

## Example

~~~~~
// Example usages
$clean = sanitizer()->pageName($dirty);
$clean = sanitizer('pageName', $dirty); // same as above
~~~~~

## Usage

~~~~~
// basic usage
$sanitizer = $functionsWireAPI->wireSanitizer();

// usage with all arguments
$sanitizer = $functionsWireAPI->wireSanitizer($name = '', $value = '');
~~~~~

## Arguments

- `$name` (optional) `string` Optionally enter a sanitizer function name
- `$value` (optional) `string` If $name populated, enter the value to sanitize

## Return value

- `Sanitizer|string|int|array|null|mixed`
