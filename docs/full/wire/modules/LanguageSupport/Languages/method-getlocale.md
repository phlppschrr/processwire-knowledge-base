# $languages->getLocale($category = LC_ALL, $language = null): string|bool

Source: `wire/modules/LanguageSupport/Languages.php`

Return the current locale setting

If using LC_ALL category and locales change by category, the returned string will be in
the format: “category=locale;category=locale”, and so on.

The first and second arguments may optionally be swapped and either can be omitted.

## Arguments

- int|Language|string|null $category Optionally specify a PHP LC constant (default=LC_ALL)
- Language|string|int|null $language Optionally return locale for specific language (default=current locale, regardless of language)

## Return value

string|bool Locale(s) string or boolean false if not supported by the system.

## Throws

- WireException if given a $language argument that is invalid

## See also

- [Languages::setLocale()](method-setlocale.md)
