# $languages->unsetLanguage(): bool

Source: `wire/modules/LanguageSupport/Languages.php`

Undo a previous setLanguage() call, restoring the previous user language

## Usage

~~~~~
// basic usage
$bool = $languages->unsetLanguage();
~~~~~

## Return value

- `bool` Returns true if language restored, false if no restore necessary

## See Also

- [Languages::setLanguage()](method-setlanguage.md)
