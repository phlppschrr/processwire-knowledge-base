# $functionsWireAPI->wireInput($type = '', $key = '', $sanitizer = null, $fallback = null): WireInput|WireInputData|array|string|int|null

Source: `wire/core/FunctionsWireAPI.php`

Access the $input API variable as a function

- Default behavior is to return the $input API var.
- If given just a $type (like "get" or "post"), it will return a WireInputData object for that type.
- If given a $type and $key it will return the input variable.
- If all arguments given, the returned value will also be run through the given sanitizer.

~~~~~
// Examples
$input = wireInput(); // Returns $input API var (WireInput)
$post = wireInput('post'); // Returns $input->post (WireInputData)
$post = wireInput()->post(); // Same as above
$value = wireInput('get', 'sort'); // Returns $input->get('sort');
$value = wireInput('get', 'sort', 'fieldName'); // Returns $input->get('sort') run through $sanitizer->fieldName().
$value = wireInput('get', 'sort', 'fieldName', 'title'); // Same as above but fallback to 'title' if no sort is present (3.0.125)
$value = wireInput('get', 'sort', ['title', 'created', 'likes'], 'title'); // Require value to be one given or fallback to 'title' (3.0.125+)
$value = wireInput()->get('sort', ['title', 'created', 'likes'], 'title'); // Same as above (3.0.125)
~~~~~

## Arguments

- string $type Optionally indicate "get", "post", "cookie" or "whitelist"
- string $key If getting a value, specify name of property containing value
- string $sanitizer Optionally specify sanitizer name to run value through, or array containing whitelist of allowed values (3.0.125).
- mixed $fallback Fallback value to return rather than null if value not present or does not validate (3.0.125+)

## Return value

WireInput|WireInputData|array|string|int|null
