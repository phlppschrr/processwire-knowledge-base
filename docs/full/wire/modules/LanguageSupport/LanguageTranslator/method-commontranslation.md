# $languageTranslator->commonTranslation($str): string

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Get a common translation

These are commonly used translations that can be used as fallbacks.

Returns blank string if given string is not a common phrase.
Returns given $str if given string is common, but not translated here.
Returns translated $str if common and translated.

## Arguments

- string $str

## Return value

string
