# $wireSessionHandler->gc($seconds): bool

Source: `wire/core/WireSessionHandler.php`

Garbage collection: remove stale sessions

## Usage

~~~~~
// basic usage
$bool = $wireSessionHandler->gc($seconds);
~~~~~

## Arguments

- `$seconds` `int` Max lifetime of a session

## Return value

- `bool` True on success, false on failure
