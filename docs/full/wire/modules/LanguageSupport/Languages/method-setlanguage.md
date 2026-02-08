# Languages::setLanguage()

Source: `wire/modules/LanguageSupport/Languages.php`

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
