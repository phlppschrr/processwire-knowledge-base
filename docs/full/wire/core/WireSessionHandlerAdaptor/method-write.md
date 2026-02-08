# $wireSessionHandlerAdaptor->write(string $id, string $data): bool

Source: `wire/core/WireSessionHandlerAdaptor.php`

Writes the session data to the session storage.

Called by `session_write_close()`, when `session_register_shutdown()` fails,
or during a normal shutdown. `close()` is called right after this function.

## Arguments

- string $id
- string $data

## Return value

bool
