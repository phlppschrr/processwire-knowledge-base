# $wire->_x($text, $context): string

Source: `wire/core/Wire.php`

Perform a language translation in a specific context

Used when to text strings might be the same in English, but different in other languages.

## Arguments

- string|array $text Text for translation.
- string $context Name of context

## Return value

string Translated text or original text if translation not available.
