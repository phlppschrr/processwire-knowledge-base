# $sanitizer->removeWhitespace($str, $options = array()): string

Source: `wire/core/Sanitizer.php`

Remove or replace all whitespace from string

## Usage

~~~~~
// basic usage
$string = $sanitizer->removeWhitespace($str);

// usage with all arguments
$string = $sanitizer->removeWhitespace($str, $options = array());
~~~~~

## Arguments

- `$str` `string` String to remove whitespace from
- `$options` (optional) `array|string` Options to modify behavior, or specify string for `replace` option: - `replace` (string): Character(s) to replace whitespace with (default=''). - `collapse` (bool): If using replace, collapse consecutive replace chars to single? (default=true) - `trim` (bool): If using replace, trim it from beginning and end? (default=true) - `html` (bool): Remove/replace HTML whitespace entities too? (default=true) - `allow` (array): Array of whitespace characters that may remain. (default=[])

## Return value

- `string`

## Since

3.0.105
