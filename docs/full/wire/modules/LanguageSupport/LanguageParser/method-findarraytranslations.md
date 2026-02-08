# $languageParser->findArrayTranslations(&$data)

Source: `wire/modules/LanguageSupport/LanguageParser.php`

Find text array values and place in alternates

This method also converts the __(['a','b','c']) array calls to single value calls like __('a')
as a pre-parser for all parsers that follow it, so they do not need to be * aware of array values
for translation calls.

## Arguments

- `$data` `string`
