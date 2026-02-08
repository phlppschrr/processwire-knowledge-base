# Languages::findOther()

Source: `wire/modules/LanguageSupport/Languages.php`

Find and return all languages except current user language

@param string|Language $selector Optionally filter by a selector string

@param Language|null $excludeLanguage optionally specify language to exclude, if not user language (can also be 1st arg)

@return PageArray
