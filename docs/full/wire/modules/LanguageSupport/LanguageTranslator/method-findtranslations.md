# $languageTranslator->findTranslations($text, $context = '', array $options = array()): array

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Find all translation(s) for given text

Scans all textdomains to find translations.

## Arguments

- string $text
- string|array $context - Optional context label for the text, to differentiate from others that may be the same in English, but not other languages. - If context is not needed you may optionally specify the $options array here.
- array $options - `getInfo` (bool): Return verbose array of information for each found translation? (default=false) - `limit` (int): Limit to this many results or 0 for no maximum (default=0)

## Return value

array - Returns array of strings containing translations of given text. - Returns array of arrays, each with verbose info, if getInfo option requested.

## Meta

- @since 3.0.237
