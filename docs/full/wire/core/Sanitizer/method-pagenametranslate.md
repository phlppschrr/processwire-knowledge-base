# $sanitizer->pageNameTranslate($value, $maxLength = 128): string

Source: `wire/core/Sanitizer.php`

Name filter for ProcessWire Page names with transliteration

This is the same as calling pageName with the `Sanitizer::translate` option for the `$beautify` argument.

## Arguments

- string $value Value to sanitize
- int $maxLength Maximum number of characters allowed in the name

## Return value

string Sanitized value
