# $session->getValFor($ns, $key, $val = null): mixed

Source: `wire/core/Session.php`

Get a session variable or return $val argument if session value not present

This is the same as get() except that it lets you specify a fallback return value in the method call.
For a namespace version use `Session::getValFor()` instead.

## Usage

~~~~~
// basic usage
$result = $session->getValFor($ns, $key);

// usage with all arguments
$result = $session->getValFor($ns, $key, $val = null);
~~~~~

## Arguments

- `$ns` `string|object` Namespace string or object
- `$key` `string` Specify variable name to retrieve
- `$val` (optional) `mixed` Fallback value if session does not have one

## Return value

- `mixed`

## Since

3.0.133
