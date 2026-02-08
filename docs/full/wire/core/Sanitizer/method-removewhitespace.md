# Sanitizer::removeWhitespace()

Source: `wire/core/Sanitizer.php`

Remove or replace all whitespace from string


@param string $str String to remove whitespace from

@param array|string $options Options to modify behavior, or specify string for `replace` option:
 - `replace` (string): Character(s) to replace whitespace with (default='').
 - `collapse` (bool): If using replace, collapse consecutive replace chars to single? (default=true)
 - `trim` (bool): If using replace, trim it from beginning and end? (default=true)
 - `html` (bool): Remove/replace HTML whitespace entities too? (default=true)
 - `allow` (array): Array of whitespace characters that may remain. (default=[])

@return string

@since 3.0.105
