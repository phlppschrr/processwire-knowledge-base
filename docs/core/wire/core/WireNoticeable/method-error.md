# $wireNoticeable->error($text, $flags = 0): $this

Source: `wire/core/Interfaces.php`

Record an non-fatal error message in the system-wide notices.

This method automatically identifies the error as coming from this class.

Fatal errors should still throw a WireException (or class derived from it)

## Arguments

- string $text
- int $flags See Notices::flags

## Return value

$this
