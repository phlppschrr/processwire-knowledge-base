# $session->getVal($key, $val = null): mixed

Source: `wire/core/Session.php`

Get a session variable or return $val argument if session value not present

This is the same as get() except that it lets you specify a fallback return value in the method call.
For a namespace version use `Session::getValFor()` instead.

## Arguments

- `$key` `string` Name of session variable to retrieve.
- `$val` (optional) `mixed` Fallback value to return if session does not have it.

## Return value

mixed Returns value of seession variable, or NULL if not found.

## Since

3.0.133
