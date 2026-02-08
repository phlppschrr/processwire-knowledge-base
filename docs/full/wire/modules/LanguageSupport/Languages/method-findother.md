# $languages->findOther($selector = '', $excludeLanguage = null): PageArray

Source: `wire/modules/LanguageSupport/Languages.php`

Find and return all languages except current user language

## Arguments

- `$selector` (optional) `string|Language` Optionally filter by a selector string
- `$excludeLanguage` (optional) `Language|null` optionally specify language to exclude, if not user language (can also be 1st arg)

## Return value

PageArray
