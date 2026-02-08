# WireTranslatable

Source: `wire/core/Interfaces.php`

Interface that indicates a class contains gettext() like translation methods

## _()

Translate the given text string into the current language if available.

If not available, or if the current language is the native language, then it returns the text as is.

@param string $text Text string to translate

@return string

## _x()

Perform a language translation in a specific context

Used when to text strings might be the same in English, but different in other languages.

@param string $text Text for translation.

@param string $context Name of context

@return string Translated text or original text if translation not available.

## _n()

Perform a language translation with singular and plural versions

@param string $textSingular Singular version of text (when there is 1 item)

@param string $textPlural Plural version of text (when there are multiple items or 0 items)

@param int $count Quantity used to determine whether singular or plural.

@return string Translated text or original text if translation not available.
