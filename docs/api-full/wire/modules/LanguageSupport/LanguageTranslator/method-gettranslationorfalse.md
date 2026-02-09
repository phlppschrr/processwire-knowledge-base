# $languageTranslator->getTranslationOrFalse($textdomain, $text, $context = '', array $options = array()): string|false

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Get translated text or boolean false if not translated (rather than default language value)

## Usage

~~~~~
// basic usage
$string = $languageTranslator->getTranslationOrFalse($textdomain, $text);

// usage with all arguments
$string = $languageTranslator->getTranslationOrFalse($textdomain, $text, $context = '', array $options = array());
~~~~~

## Arguments

- `$textdomain` `string|object` Textdomain string, filename, or object.
- `$text` `string` Text in default language (EN) that needs to be converted to current language.
- `$context` (optional) `string` Optional context label for the text, to differentiate from others that may be the same in English, but not other languages.
- `$options` (optional) `array`

## Return value

- `string|false`

## Since

3.0.237
