# PageProperties

Source: `wire/core/PageProperties.php`

## Summary

ProcessWire Page properties helper

Common methods:
- [`statusToNames()`](method-statustonames.md)

For static runtime property detection by the base Page class.
The properties/methods in this class were originally in the base Page class
but have been moved here for Page class load time optimization purposes.
Except where indicated, please treat these properties as private to the
Page class.

## Methods
- [`statusToNames(int $status): array`](method-statustonames.md) Given a status (flags int) return array of status names
