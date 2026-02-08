# FunctionsWireAPI::wireInputGet()

Source: `wire/core/FunctionsWireAPI.php`

Access the $input->get API variable as a function

This is the same as the input() function except that the $type "get" is already implied.

@param string $key Name of input variable to get

@param string $sanitizer Optionally specify sanitizer name to run value through, or array containing whitelist of allowed values (3.0.125+).

@param mixed $fallback Fallback value to return rather than null if value not present or does not validate (3.0.125+)

@return WireInputData|string|int|array|null
