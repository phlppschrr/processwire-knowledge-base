# Sanitizer::pageNameTranslate()

Source: `wire/core/Sanitizer.php`

Name filter for ProcessWire Page names with transliteration

This is the same as calling pageName with the `Sanitizer::translate` option for the `$beautify` argument.


@param string $value Value to sanitize

@param int $maxLength Maximum number of characters allowed in the name

@return string Sanitized value
