# WireSessionHandlerAdaptor::gc()

Source: `wire/core/WireSessionHandlerAdaptor.php`

Cleans up expired sessions.

Called by `session_start()`, based on `session.gc_divisor`,
`session.gc_probability` and `session.gc_maxlifetime` settings.

@param int $max_lifetime

@return int|false
