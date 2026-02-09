# WireNoticeable

Source: `wire/core/Interfaces.php`

## Summary

Interface that indicates the class supports Notice messaging

Common methods:
- [`message()`](method-message.md)
- [`error()`](method-error.md)

## Methods
- [`message(string $text, int $flags = 0): $this`](method-message.md) Record an informational or 'success' message in the system-wide notices.
- [`error(string $text, int $flags = 0): $this`](method-error.md) Record an non-fatal error message in the system-wide notices.
