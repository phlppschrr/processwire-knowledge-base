# $languages->setDefault(?Language $language = null): void

Source: `wire/modules/LanguageSupport/Languages.php`

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

## Arguments

- `$language` (optional) `Language|null`

## Return value

void

## See also

- [Languages::unsetDefault()](method-unsetdefault.md)
- [Languages::setLanguage()](method-setlanguage.md)
