# WireNoticeable

Source: `wire/core/Interfaces.php`

Interface that indicates the class supports Notice messaging

## message()

Record an informational or 'success' message in the system-wide notices.

This method automatically identifies the message as coming from this class.

@param string $text

@param int $flags See Notices::flags

@return $this

## error()

Record an non-fatal error message in the system-wide notices.

This method automatically identifies the error as coming from this class.

Fatal errors should still throw a WireException (or class derived from it)

@param string $text

@param int $flags See Notices::flags

@return $this
