# $sanitizer->name($value, $beautify = false, $maxLength = 128, $replacement = '_', $options = array()): string

Source: `wire/core/Sanitizer.php`

Sanitize in "name" format (ASCII alphanumeric letters/digits, hyphens, underscores, periods)

Default behavior:

- Allows both upper and lowercase ASCII letters.
- Limits maximum length to 128 characters.
- Replaces non-name format characters with underscore "_".

~~~~~
$test = "Foo+Bar Baz-123"
echo $sanitizer->name($test); // outputs: Foo_Bar_Baz-123
~~~~~

## Arguments

- `$value` `string` Value that you want to convert to name format.
- `$beautify` (optional) `bool|int` Beautify the returned name? - Beautify makes returned name prettier by getting rid of doubled punctuation, leading/trailing punctuation and such. - Should be TRUE when creating a resource using the name for the first time (default is FALSE). - You may also specify the constant `Sanitizer::translate` (or integer 2) for the this argument, which will make it translate letters based on name format settings in ProcessWire.
- `$maxLength` (optional) `int` Maximum number of characters allowed in the name (default=128).
- `$replacement` (optional) `string` Replacement character for invalid characters. Should be either "_", "-" or "." (default="_").
- `$options` (optional) `array` Extra options to replace default 'beautify' behaviors - `allowAdjacentExtras` (bool): Whether to allow [-_.] characters next to each other (default=false). - `allowDoubledReplacement` (bool): Whether to allow two of the same replacement chars [-_] next to each other (default=false). - `allowedExtras (array): Specify extra allowed characters (default=`['-', '_', '.']`).

## Return value

string Sanitized value in name format

## See also

- [Sanitizer::pageName()](method-pagename.md)
