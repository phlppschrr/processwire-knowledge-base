# $functionsAPI->input($type = '', $key = '', $sanitizer = null, $fallback = null): WireInput|WireInputData|array|string|int|null

Source: `wire/core/FunctionsAPI.php`

Access GET, POST or COOKIE input variables and more ($input API variable as a function)

- Default behavior with no arguments is to return the `$input` API variable.
- If given just a `$type` argument (like “get” or “post”), it will return a `WireInputData` object for that type.
- If given a `$type` and `$key` arguments, it will return the value, or null if not present.
- If `$sanitizer` argument given, the returned value will also be run through the given sanitizer.
- If the `$sanitizer` argument is an array, the returned input value must be within the given list, or null if not (3.0.125+).
- If `$fallback` argument given, it will return the fallback value if input value was not present or not valid (3.0.125+).
- See the `WireInput::get()` method for all options.

## Example

~~~~~
// Can be used the same way as the $input API variable
// In examples below the “post” can also be “get” or “cookie”
$input = input(); // Returns $input API var (WireInput)
$post = input()->post(); // Returns $input->post (WireInputData instance)
$foo = input()->post('foo'); // Returns POST variable “foo”
$bar = input()->post('bar', 'text'); // Returns “bar” after text sanitizer (3.0.125+)
$s = input()->post('s', ['foo', 'bar', 'baz']); // POST var “s” must match given list (3.0.125+)

// You can also move the arguments all to the function call if you prefer:
$s = input('get', 'sort'); // Returns GET var “sort”
$s = input('get', 'sort', 'fieldName'); // Returns “sort” after “fieldName” sanitizer
$s = input('get', 'sort', ['title', 'created']); // Require sort to be one in given array (3.0.125+)
$s = input('get', 'sort', ['title', 'created'], 'title'); // Same as above, fallback to 'title' (3.0.125+)
~~~~~

## Usage

~~~~~
// basic usage
$wireInput = $functionsAPI->input();

// usage with all arguments
$wireInput = $functionsAPI->input($type = '', $key = '', $sanitizer = null, $fallback = null);
~~~~~

## Arguments

- `$type` (optional) `string` Optionally indicate "get", "post", "cookie" or "whitelist"
- `$key` (optional) `string` If getting a value, specify name of input property containing value
- `$sanitizer` (optional) `string` Optionally specify sanitizer name to run value through, or in 3.0.125+ may also be an array of allowed values.
- `$fallback` (optional) `string|int|null` Value to fallback to if input not present or invalid

## Return value

- `WireInput|WireInputData|array|string|int|null`

## See Also

- WireInput
