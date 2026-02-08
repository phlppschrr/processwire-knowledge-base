# $sanitizer->removeWhitespace($str, $options = array()): string

Source: `wire/core/Sanitizer.php`

Remove or replace all whitespace from string

## Arguments

- string $str String to remove whitespace from
- array|string $options Options to modify behavior, or specify string for `replace` option: - `replace` (string): Character(s) to replace whitespace with (default=''). - `collapse` (bool): If using replace, collapse consecutive replace chars to single? (default=true) - `trim` (bool): If using replace, trim it from beginning and end? (default=true) - `html` (bool): Remove/replace HTML whitespace entities too? (default=true) - `allow` (array): Array of whitespace characters that may remain. (default=[])

## Return value

string

## Meta

- @since 3.0.105
