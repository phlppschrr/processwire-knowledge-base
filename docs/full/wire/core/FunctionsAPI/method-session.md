# $functionsAPI->session($key = '', $value = null): Session|null|string|array|int|float

Source: `wire/core/FunctionsAPI.php`

Get or set values in the current user session ($session API variable as a function)

This function behaves the same as the `$session` API variable, though does support
optional shortcut arguments for getting or setting values.

~~~~~
// Get a value from the session
$foo = session()->foo; // direct syntax
$foo = session()->get('foo'); // regular syntax
$foo = session('foo'); // shortcut syntax

// Set a value to the session
session()->foo = 'bar'; // direct syntax
session()->set('foo', 'bar');  // regular syntax
session('foo', 'bar'); // shortcut syntax
~~~~~

## Arguments

- `$key` (optional) `string` Optional property to get or set
- `$value` (optional) `null` Optional value to set

## Return value

Session|null|string|array|int|float

## See also

- Session
