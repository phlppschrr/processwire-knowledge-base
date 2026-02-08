# Wire::_n()

Source: `wire/core/Wire.php`

Perform a language translation with singular and plural versions


@param string $textSingular Singular version of text (when there is 1 item).

@param string $textPlural Plural version of text (when there are multiple items or 0 items).

@param int $count Quantity used to determine whether singular or plural.

@return string Translated text or original text if translation not available.
