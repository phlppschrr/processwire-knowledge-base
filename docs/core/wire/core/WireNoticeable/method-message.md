# WireNoticeable::message()

Source: `wire/core/Interfaces.php`

Record an informational or 'success' message in the system-wide notices.

This method automatically identifies the message as coming from this class.

@param string $text

@param int $flags See Notices::flags

@return $this
