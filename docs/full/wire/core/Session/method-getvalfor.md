# $session->getValFor($ns, $key, $val = null): mixed

Source: `wire/core/Session.php`

Get a session variable or return $val argument if session value not present

This is the same as get() except that it lets you specify a fallback return value in the method call.
For a namespace version use `Session::getValFor()` instead.

## Arguments

- string|object $ns Namespace string or object
- string $key Specify variable name to retrieve
- mixed $val Fallback value if session does not have one

## Return value

mixed

## Meta

- @since 3.0.133
