# Languages

Source: `wire/modules/LanguageSupport/Languages.php`

ProcessWire Languages (plural) Class

API variable $languages enables access to all Language pages and various helper methods.
The $languages API variable is most commonly used for iteration of all installed languages.
~~~~~
foreach($languages as $language) {
  echo "<li>$language->title ($language->name) ";
  if($language->id == $user->language->id) {
    echo "current"; // the user's current language
  }
  echo "</li>";
}
~~~~~


ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@property Language $default Get default language

@property Language $getDefault Get default language (alias of $default)

@method added(Page $language) Hook called when Language is added

@method deleted(Page $language) Hook called when Language is deleted

@method updated(Page $language, $what) Hook called when Language is added or deleted

@method languageChanged($fromLanguage, $toLanguage) Hook called when User language is changed

## __construct()

Construct

@param ProcessWire $wire

@param array $templates

@param array $parents

## translator()

Return the LanguageTranslator instance for the given language

@param Language $language

@return LanguageTranslator

## findOther()

Find and return all languages except current user language

@param string|Language $selector Optionally filter by a selector string

@param Language|null $excludeLanguage optionally specify language to exclude, if not user language (can also be 1st arg)

@return PageArray

## findNonDefault()

Find and return all languages except default language

@param string $selector Optionally filter by a selector string

@return PageArray

## getDefault()

Get the default language

The default language can also be accessed from property `$languages->default`.

~~~~~
if($user->language->id == $languages->getDefault()->id) {
  // user has the default language
}
~~~~~

@return Language

@throws WireException when default language hasn't yet been set

## setDefault()

Set current user to have default language temporarily

If given no arguments, it sets the current `$user` to have the default language temporarily. It is
expected you will follow it up with a later call to `$languages->unsetDefault()` to restore the
previous language the user had.

If given a Language object, it sets that as the default language (for internal use only).

~~~~~
// set current user to have default language
$languages->setDefault();
// perform some operation that has a default language dependency ...
// then restore the user's previous language with unsetDefault()
$languages->unsetDefault();
~~~~~

@param Language|null $language

@return void

@see Languages::unsetDefault(), Languages::setLanguage()

## unsetDefault()

Restores whatever previous language a user had prior to a setDefault() call

@return void

@see Languages::setDefault()

## setLanguage()

Set the current user language for the current request

This also remembers the previous Language setting which can be restored with
a `$languages->unsetLanguage()` call.

~~~~~
$languages->setLanguage('de');
~~~~~

@param int|string|Language $language Language id, name or Language object

@return bool Returns false if no change necessary, true if language was changed

@throws WireException if given $language argument doesn't resolve

@see Languages::unsetLanguage()

## getLanguage()

Get the current language or optionally a specific named language

- This method is not entirely necessary but is here to accompany the setLanguage() method for syntax convenience.
- If you specify a `$name` argument, this method works the same as the `$languages->get($name)` method.
- If you call with no arguments, it returns the current user language, same as `$user->language`, but using this
  method may be preferable in some contexts, depending on how your IDE understands API calls.

@param string|int $name Specify language name (or ID) to get a specific language, or omit to get current language

@return Language|null

@since 3.0.127

## unsetLanguage()

Undo a previous setLanguage() call, restoring the previous user language

@return bool Returns true if language restored, false if no restore necessary

@see Languages::setLanguage()

## setLocale()

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

@param int|string|array|null|Language $category Specify a PHP “LC_” constant (int) or omit (or null) for default (LC_ALL).

@param int|string|array|null|Language $locale Specify string, array or CSV string of locale name(s),
  omit (null) for current language locale, or specify Language object to pull locale from that language.

@return string|bool Returns the locale that was set or boolean false if requested locale cannot be set.

@see Languages::getLocale()

## getLocale()

Return the current locale setting

If using LC_ALL category and locales change by category, the returned string will be in
the format: “category=locale;category=locale”, and so on.

The first and second arguments may optionally be swapped and either can be omitted.

@param int|Language|string|null $category Optionally specify a PHP LC constant (default=LC_ALL)

@param Language|string|int|null $language Optionally return locale for specific language (default=current locale, regardless of language)

@return string|bool Locale(s) string or boolean false if not supported by the system.

@see Languages::setLocale()

@throws WireException if given a $language argument that is invalid

## ___deleted()

Hook called when a language is deleted


@param Page $language

## ___added()

Hook called when a language is added


@param Page $language

## ___updated()

Hook called when a language is added or deleted


@param Page $language

@param string $what What occurred? ('added' or 'deleted')

## pageNames()

Get LanguageSupportPageNames module if installed, false if not

@return LanguageSupportPageNames|false

@since 3.0.186

## hasPageNames()

Is LanguageSupportPageNames installed?

@return bool

@since 3.0.186

## editable()

Does current user have edit access for page fields in given language?

@param Language|int|string $language Language id, name or object, or string "none" to refer to non-multi-language fields

@return bool True if editable, false if not

## importTranslationsFile()

Import a language translations file

@param Language|string $language

@param string $file Full path to .csv translations file
  The .csv file must be one generated by ProcessWire’s language translation tools.

@param bool $quiet Specify true to suppress error/success notifications being generated (default=false)

@return bool|int Returns integer with number of translations imported or boolean false on error

@throws WireException

@since 3.0.181
