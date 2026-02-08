# $wireTranslatable->_n($textSingular, $textPlural, $count): string

Source: `wire/core/Interfaces.php`

Perform a language translation with singular and plural versions

## Arguments

- string $textSingular Singular version of text (when there is 1 item)
- string $textPlural Plural version of text (when there are multiple items or 0 items)
- int $count Quantity used to determine whether singular or plural.

## Return value

string Translated text or original text if translation not available.
