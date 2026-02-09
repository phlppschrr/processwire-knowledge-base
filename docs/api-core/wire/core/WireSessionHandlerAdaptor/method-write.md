# $wireSessionHandlerAdaptor->write(string $id, string $data): bool

Source: `wire/core/WireSessionHandlerAdaptor.php`

Writes the session data to the session storage.

Called by `session_write_close()`, when `session_register_shutdown()` fails,
or during a normal shutdown. `close()` is called right after this function.

## Usage

~~~~~
// basic usage
$bool = $wireSessionHandlerAdaptor->write($id, $data);

// usage with all arguments
$bool = $wireSessionHandlerAdaptor->write(string $id, string $data);
~~~~~

## Arguments

- `$id` `string`
- `$data` `string`

## Return value

- `bool`
