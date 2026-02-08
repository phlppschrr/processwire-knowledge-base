# $languageTranslator->textdomainToFilename($textdomain): string

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Given a textdomain string, convert it to a filename (relative to site root)

This is determined by loading the textdomain and then grabbing the filename stored in the JSON properties

## Arguments

- `$textdomain` `string`

## Return value

string
