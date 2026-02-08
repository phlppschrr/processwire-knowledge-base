# $wireSessionHandlerAdaptor->gc(int $max_lifetime): int|false

Source: `wire/core/WireSessionHandlerAdaptor.php`

Cleans up expired sessions.

Called by `session_start()`, based on `session.gc_divisor`,
`session.gc_probability` and `session.gc_maxlifetime` settings.

## Usage

~~~~~
// basic usage
$int = $wireSessionHandlerAdaptor->gc($max_lifetime);

// usage with all arguments
$int = $wireSessionHandlerAdaptor->gc(int $max_lifetime);
~~~~~

## Arguments

- `$max_lifetime` `int`

## Return value

- `int|false`
