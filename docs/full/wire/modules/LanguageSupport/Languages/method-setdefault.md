# Languages::setDefault()

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

@param Language|null $language

@return void

@see Languages::unsetDefault(), Languages::setLanguage()
