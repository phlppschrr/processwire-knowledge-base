# WireSessionHandlerAdaptor::destroy()

Source: `wire/core/WireSessionHandlerAdaptor.php`

Destroys a session.

Called by `session_regenerate_id()` (with `$destroy = true`),
`session_destroy()` and when `session_decode()` fails.

@param string $id

@return bool
