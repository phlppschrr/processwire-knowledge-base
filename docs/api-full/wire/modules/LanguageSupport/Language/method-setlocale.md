# $language->setLocale($category = LC_ALL): string|bool

Source: `wire/modules/LanguageSupport/Language.php`

Set the current locale to use settings defined for this language

See the `Languages::setLocale()` method for full details.

## Usage

~~~~~
// basic usage
$string = $language->setLocale();

// usage with all arguments
$string = $language->setLocale($category = LC_ALL);
~~~~~

## Arguments

- `$category` (optional) `int` Optional category (default=LC_ALL)

## Return value

- `string|bool` Returns the locale that was set or boolean false if requested locale cannot be set.

## See Also

- [Languages::setLocale()](../Languages/method-setlocale.md)
