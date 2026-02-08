# $wireSessionHandlerAdaptor->close(): bool

Source: `wire/core/WireSessionHandlerAdaptor.php`

Closes the current session.

This function is automatically executed when closing the session,
or explicitly via `session_write_close()`.

## Usage

~~~~~
// basic usage
$bool = $wireSessionHandlerAdaptor->close();
~~~~~

## Return value

- `bool`
