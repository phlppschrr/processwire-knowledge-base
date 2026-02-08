# $sanitizer->camelCase($value, array $options = array()): string

Source: `wire/core/Sanitizer.php`

Convert string to be all camelCase

For example, "Hello World" becomes "helloWorld" or "foo-bar-baz" becomes "fooBarBaz".

## Arguments

- `$value` `string`
- `$options` (optional) `array` - `allow` (string): Characters to allow or range of characters to allow, for placement in regex (default='a-zA-Z0-9'). - `allowUnderscore` (bool): Allow underscore characters? (default=false) - `startLowercase` (bool): Always start return value with lowercase character? (default=true) - `startNumber` (bool): Allow return value to begin with a number? (default=false)

## Return value

string
