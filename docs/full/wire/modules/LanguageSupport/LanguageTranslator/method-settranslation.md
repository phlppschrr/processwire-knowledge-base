# $languageTranslator->setTranslation($textdomain, $text, $translation, $context = ''): string

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Set a translation

## Usage

~~~~~
// basic usage
$string = $languageTranslator->setTranslation($textdomain, $text, $translation);

// usage with all arguments
$string = $languageTranslator->setTranslation($textdomain, $text, $translation, $context = '');
~~~~~

## Arguments

- `$textdomain` `string`
- `$text` `string`
- `$translation` `string`
- `$context` (optional) `string`

## Return value

- `string`
