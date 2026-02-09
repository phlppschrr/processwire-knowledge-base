# $languages->setLanguage($language): bool

Source: `wire/modules/LanguageSupport/Languages.php`

Set the current user language for the current request

This also remembers the previous Language setting which can be restored with
a `$languages->unsetLanguage()` call.

## Example

~~~~~
$languages->setLanguage('de');
~~~~~

## Usage

~~~~~
// basic usage
$bool = $languages->setLanguage($language);
~~~~~

## Arguments

- `$language` `int|string|Language` Language id, name or Language object

## Return value

- `bool` Returns false if no change necessary, true if language was changed

## Exceptions

- `WireException` if given $language argument doesn't resolve

## See Also

- [Languages::unsetLanguage()](method-unsetlanguage.md)
