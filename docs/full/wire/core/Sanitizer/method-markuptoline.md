# $sanitizer->markupToLine($value, array $options = array()): string

Source: `wire/core/Sanitizer.php`

Convert a string containing markup or entities to be a single line of plain text

This is the same as the `$sanitizer->markupToText()` method except that the return
value is always just a single line.

## Arguments

- `$value` `string` Value to convert
- `$options` (optional) `array` Options to modify default behavior: - `newline` (string): Character(s) to replace newlines with (default=" "). - `separator` (string): Character(s) to separate HTML <li> items with (default=", "). - `entities` (bool): Entity encode returned value? (default=false). - `trim` (string): Character(s) to trim from beginning and end of value (default=" -,:;|\n\t").

## Return value

string Converted string of text on a single line
