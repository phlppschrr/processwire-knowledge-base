# $languageTranslator->textdomainTemplate($file = '', $textdomain = '', array $translations = array()): array

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Return the array template for a textdomain, optionally populating it with data

## Usage

~~~~~
// basic usage
$array = $languageTranslator->textdomainTemplate();

// usage with all arguments
$array = $languageTranslator->textdomainTemplate($file = '', $textdomain = '', array $translations = array());
~~~~~

## Arguments

- `$file` (optional) `string`
- `$textdomain` (optional) `string`
- `$translations` (optional) `array`

## Return value

- `array`
