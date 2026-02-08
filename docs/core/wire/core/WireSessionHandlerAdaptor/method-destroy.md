# $wireSessionHandlerAdaptor->destroy(string $id): bool

Source: `wire/core/WireSessionHandlerAdaptor.php`

Destroys a session.

Called by `session_regenerate_id()` (with `$destroy = true`),
`session_destroy()` and when `session_decode()` fails.

## Arguments

- `$id` `string`

## Return value

bool
