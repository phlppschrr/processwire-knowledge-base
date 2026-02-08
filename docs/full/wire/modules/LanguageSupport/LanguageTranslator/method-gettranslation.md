# $languageTranslator->getTranslation($textdomain, $text, $context = '', array $options = array()): string|array|false

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Perform a translation in the given $textdomain for $text to the current language

## Usage

~~~~~
// basic usage
$string = $languageTranslator->getTranslation($textdomain, $text);

// usage with all arguments
$string = $languageTranslator->getTranslation($textdomain, $text, $context = '', array $options = array());
~~~~~

## Arguments

- `$textdomain` `string|object` Textdomain string, filename, or object.
- `$text` `string` Text in default language (EN) that needs to be converted to current language.
- `$context` (optional) `string` Optional context label for the text, to differentiate from others that may be the same in English, but not other languages.
- `$options` (optional) `array` 3.0.237+ only - `getInfo` (bool): Get verbose array of info about translation? (default=false) - `getFalse` (bool): Return false rather than default language value if translation not found? (default=false)

## Return value

- `string|array|false` Translation if available, or original EN version if translation not available. - Returns array if options[getInfo] is true. - Returns false if translation not found and options[getFalse] is true.
