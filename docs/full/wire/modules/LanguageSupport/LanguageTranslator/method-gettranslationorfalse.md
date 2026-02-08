# LanguageTranslator::getTranslationOrFalse()

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Get translated text or boolean false if not translated (rather than default language value)

@param string|object $textdomain Textdomain string, filename, or object.

@param string $text Text in default language (EN) that needs to be converted to current language.

@param string $context Optional context label for the text, to differentiate from others that may be the same in English, but not other languages.

@param array $options

@return string|false

@since 3.0.237
