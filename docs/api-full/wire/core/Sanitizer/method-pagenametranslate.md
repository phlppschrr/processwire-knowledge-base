# $sanitizer->pageNameTranslate($value, $maxLength = 128): string

Source: `wire/core/Sanitizer.php`

Name filter for ProcessWire Page names with transliteration

This is the same as calling pageName with the `Sanitizer::translate` option for the `$beautify` argument.

## Usage

~~~~~
// basic usage
$string = $sanitizer->pageNameTranslate($value);

// usage with all arguments
$string = $sanitizer->pageNameTranslate($value, $maxLength = 128);
~~~~~

## Arguments

- `$value` `string` Value to sanitize
- `$maxLength` (optional) `int` Maximum number of characters allowed in the name

## Return value

- `string` Sanitized value
