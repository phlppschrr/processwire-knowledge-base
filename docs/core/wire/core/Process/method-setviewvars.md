# Process::setViewVars()

Source: `wire/core/Process.php`

Set a variable that will be passed to the output view.

You can also do this by having your execute() method(s) return an associative array of
variables to send to the view file.


@param string|array $key Property to set, or array of `[property => value]` to set (leaving 2nd argument as null)

@param mixed|null $value Value to set

@return $this

@throws WireException if given an invalid type for $key
