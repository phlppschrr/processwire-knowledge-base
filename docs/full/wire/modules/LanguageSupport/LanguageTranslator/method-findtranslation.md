# $languageTranslator->findTranslation($text, $context = '', array $options = array()): string|array

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Find a translation for given text

Scans all textdomains to find first translation.

## Usage

~~~~~
// basic usage
$string = $languageTranslator->findTranslation($text);

// usage with all arguments
$string = $languageTranslator->findTranslation($text, $context = '', array $options = array());
~~~~~

## Arguments

- `$text` `string`
- `$context` (optional) `string|array` - Optional context label for the text, to differentiate from others that may be the same in English, but not other languages. - If context is not needed you may optionally specify the $options array here.
- `$options` (optional) `array` - `getInfo` (bool): Return verbose array of information about found translation? (default=false)

## Return value

- `string|array` - Returns string with translated text if found, or blank string if not found. - Returns array of info if getInfo option requested. This array is empty if translation was not found.

## Since

3.0.237
