# Languages: other

Source: `wire/modules/LanguageSupport/Languages.php`

@property Language $default Get default language

@property Language $getDefault Get default language (alias of $default)

@method added(Page $language) Hook called when Language is added

@method deleted(Page $language) Hook called when Language is deleted

@method updated(Page $language, $what) Hook called when Language is added or deleted

@method languageChanged($fromLanguage, $toLanguage) Hook called when User language is changed
