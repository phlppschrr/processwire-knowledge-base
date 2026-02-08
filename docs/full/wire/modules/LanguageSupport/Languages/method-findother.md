# $languages->findOther($selector = '', $excludeLanguage = null): PageArray

Source: `wire/modules/LanguageSupport/Languages.php`

Find and return all languages except current user language

## Arguments

- string|Language $selector Optionally filter by a selector string
- Language|null $excludeLanguage optionally specify language to exclude, if not user language (can also be 1st arg)

## Return value

PageArray
