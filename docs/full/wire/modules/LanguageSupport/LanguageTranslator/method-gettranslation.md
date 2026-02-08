# LanguageTranslator::getTranslation()

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Perform a translation in the given $textdomain for $text to the current language

@param string|object $textdomain Textdomain string, filename, or object.

@param string $text Text in default language (EN) that needs to be converted to current language.

@param string $context Optional context label for the text, to differentiate from others that may be the same in English, but not other languages.

@param array $options 3.0.237+ only
 - `getInfo` (bool): Get verbose array of info about translation? (default=false)
 - `getFalse` (bool): Return false rather than default language value if translation not found? (default=false)

@return string|array|false Translation if available, or original EN version if translation not available.
 - Returns array if options[getInfo] is true.
 - Returns false if translation not found and options[getFalse] is true.
