# Session::getValFor()

Source: `wire/core/Session.php`

Get a session variable or return $val argument if session value not present

This is the same as get() except that it lets you specify a fallback return value in the method call.
For a namespace version use `Session::getValFor()` instead.


@param string|object $ns Namespace string or object

@param string $key Specify variable name to retrieve

@param mixed $val Fallback value if session does not have one

@return mixed

@since 3.0.133
