# Languages::getLocale()

Source: `wire/modules/LanguageSupport/Languages.php`

Return the current locale setting

If using LC_ALL category and locales change by category, the returned string will be in
the format: “category=locale;category=locale”, and so on.

The first and second arguments may optionally be swapped and either can be omitted.

@param int|Language|string|null $category Optionally specify a PHP LC constant (default=LC_ALL)

@param Language|string|int|null $language Optionally return locale for specific language (default=current locale, regardless of language)

@return string|bool Locale(s) string or boolean false if not supported by the system.

@see Languages::setLocale()

@throws WireException if given a $language argument that is invalid
