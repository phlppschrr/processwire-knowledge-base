# $process->setViewVars($key, $value = null): $this

Source: `wire/core/Process.php`

Set a variable that will be passed to the output view.

You can also do this by having your execute() method(s) return an associative array of
variables to send to the view file.

## Arguments

- string|array $key Property to set, or array of `[property => value]` to set (leaving 2nd argument as null)
- mixed|null $value Value to set

## Return value

$this

## Throws

- WireException if given an invalid type for $key
