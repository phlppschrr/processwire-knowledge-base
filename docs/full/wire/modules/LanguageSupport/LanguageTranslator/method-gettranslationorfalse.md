# $languageTranslator->getTranslationOrFalse($textdomain, $text, $context = '', array $options = array()): string|false

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Get translated text or boolean false if not translated (rather than default language value)

## Arguments

- string|object $textdomain Textdomain string, filename, or object.
- string $text Text in default language (EN) that needs to be converted to current language.
- string $context Optional context label for the text, to differentiate from others that may be the same in English, but not other languages.
- array $options

## Return value

string|false

## Meta

- @since 3.0.237
