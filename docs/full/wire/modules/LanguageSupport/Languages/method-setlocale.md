# $languages->setLocale($category = LC_ALL, $locale = null): string|bool

Source: `wire/modules/LanguageSupport/Languages.php`

Set the current locale

This function behaves exactly the same way as [PHP setlocale](http://php.net/manual/en/function.setlocale.php) except
for the following:

- If the $locale argument is omitted, it uses the locale setting translated for the current user language.
- You can optionally specify a CSV string of locales to try for the $locale argument.
- You can optionally or a “category=locale;category=locale;category=locale” string for the $locale argument.
  When this type of string is used, the $category argument is ignored.
- This method does not accept more than the 3 indicated arguments.
- Any of the arguments may be swapped.

See the PHP setlocale link above for a list of constants that can be used for the `$category` argument.

Note that the locale is set once at bootup by ProcessWire, and does not change after that unless you call this
method. Meaning, a change to `$user->language` does not automatically change the locale. If you want to change
the locale, you would have to call this method after changing the user’s language from the API side.

~~~~~
// Set locale to whatever settings defined for current $user language
$languages->setLocale();

// Set all locale categories
$languages->setLocale(LC_ALL, 'en_US.UTF-8');

// Set locale for specific category (CTYPE)
$languages->setLocale(LC_CTYPE, 'en_US.UTF-8');

// Try multiple locales till one works (in order) using array
$languages->setLocale(LC_ALL, [ 'en_US.UTF-8', 'en_US', 'en' ]);

// Same as above, except using CSV string
$languages->setLocale(LC_ALL, 'en_US.UTF-8, en_US, en');

// Set multiple categories and locales (first argument ignored)
$languages->setLocale(null, 'LC_CTYPE=en_US;LC_NUMERIC=de_DE;LC_TIME=es_ES');
~~~~~

## Arguments

- int|string|array|null|Language $category Specify a PHP “LC_” constant (int) or omit (or null) for default (LC_ALL).
- int|string|array|null|Language $locale Specify string, array or CSV string of locale name(s), omit (null) for current language locale, or specify Language object to pull locale from that language.

## Return value

string|bool Returns the locale that was set or boolean false if requested locale cannot be set.

## See also

- [Languages::getLocale()](method-getlocale.md)
