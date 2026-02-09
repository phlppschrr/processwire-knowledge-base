# $wireTranslatable->_n($textSingular, $textPlural, $count): string

Source: `wire/core/Interfaces.php`

Perform a language translation with singular and plural versions

## Usage

~~~~~
// basic usage
$string = $wireTranslatable->_n($textSingular, $textPlural, $count);
~~~~~

## Arguments

- `$textSingular` `string` Singular version of text (when there is 1 item)
- `$textPlural` `string` Plural version of text (when there are multiple items or 0 items)
- `$count` `int` Quantity used to determine whether singular or plural.

## Return value

- `string` Translated text or original text if translation not available.
