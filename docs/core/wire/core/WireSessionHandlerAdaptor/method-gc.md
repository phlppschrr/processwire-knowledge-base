# $wireSessionHandlerAdaptor->gc(int $max_lifetime): int|false

Source: `wire/core/WireSessionHandlerAdaptor.php`

Cleans up expired sessions.

Called by `session_start()`, based on `session.gc_divisor`,
`session.gc_probability` and `session.gc_maxlifetime` settings.

## Arguments

- `$max_lifetime` `int`

## Return value

int|false
