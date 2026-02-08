# $languages->setLanguage($language): bool

Source: `wire/modules/LanguageSupport/Languages.php`

Set the current user language for the current request

This also remembers the previous Language setting which can be restored with
a `$languages->unsetLanguage()` call.

~~~~~
$languages->setLanguage('de');
~~~~~

## Arguments

- int|string|Language $language Language id, name or Language object

## Return value

bool Returns false if no change necessary, true if language was changed

## Throws

- WireException if given $language argument doesn't resolve

## See also

- [Languages::unsetLanguage()](method-unsetlanguage.md)
