# $sanitizer->removeMB4($value, array $options = array()): string|array

Source: `wire/core/Sanitizer.php`

Removes 4-byte UTF-8 characters (like emoji) that produce error with with MySQL regular “UTF8” encoding

Returns the same value type that it is given. If given something other than a string or array, it just
returns it without modification.

## Arguments

- `$value` `string|array` String or array containing strings
- `$options` (optional) `array` Options to modify behavior, 3.0.169+ only: - `replaceWith` (string): Replace MB4+ characters with this character, may not be blank (default='�') - `version` (int): Replacement method version (default=2)

## Return value

string|array
