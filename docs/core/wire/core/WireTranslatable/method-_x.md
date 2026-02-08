# $wireTranslatable->_x($text, $context): string

Source: `wire/core/Interfaces.php`

Perform a language translation in a specific context

Used when to text strings might be the same in English, but different in other languages.

## Usage

~~~~~
// basic usage
$string = $wireTranslatable->_x($text, $context);
~~~~~

## Arguments

- `$text` `string` Text for translation.
- `$context` `string` Name of context

## Return value

- `string` Translated text or original text if translation not available.
