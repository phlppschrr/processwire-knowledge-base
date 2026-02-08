# $wire->_($text): string

Source: `wire/core/Wire.php`

Translate the given text string into the current language if available.

If not available, or if the current language is the native language, then it returns the text as is.

## Usage

~~~~~
// basic usage
$string = $wire->_($text);
~~~~~

## Arguments

- `$text` `string|array` Text string to translate (or array in 3.0.151 also supported)

## Return value

- `string`
