# LanguageTranslator::findTranslation()

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Find a translation for given text

Scans all textdomains to find first translation.

@param string $text

@param string|array $context
  - Optional context label for the text, to differentiate from others that may be the same in English, but not other languages.
  - If context is not needed you may optionally specify the $options array here.

@param array $options
 - `getInfo` (bool): Return verbose array of information about found translation? (default=false)

@return string|array
  - Returns string with translated text if found, or blank string if not found.
  - Returns array of info if getInfo option requested. This array is empty if translation was not found.

@since 3.0.237
