# $functionsWireAPI->wireInputGet($key = '', $sanitizer = null, $fallback = null): WireInputData|string|int|array|null

Source: `wire/core/FunctionsWireAPI.php`

Access the $input->get API variable as a function

This is the same as the input() function except that the $type "get" is already implied.

## Arguments

- `$key` (optional) `string` Name of input variable to get
- `$sanitizer` (optional) `string` Optionally specify sanitizer name to run value through, or array containing whitelist of allowed values (3.0.125+).
- `$fallback` (optional) `mixed` Fallback value to return rather than null if value not present or does not validate (3.0.125+)

## Return value

WireInputData|string|int|array|null
