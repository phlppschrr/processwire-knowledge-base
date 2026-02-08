# Sanitizer::removeMB4()

Source: `wire/core/Sanitizer.php`

Removes 4-byte UTF-8 characters (like emoji) that produce error with with MySQL regular “UTF8” encoding

Returns the same value type that it is given. If given something other than a string or array, it just
returns it without modification.


@param string|array $value String or array containing strings

@param array $options Options to modify behavior, 3.0.169+ only:
 - `replaceWith` (string): Replace MB4+ characters with this character, may not be blank (default='�')
 - `version` (int): Replacement method version (default=2)

@return string|array
