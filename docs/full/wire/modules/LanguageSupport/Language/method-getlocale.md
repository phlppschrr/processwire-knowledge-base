# $language->getLocale($category = LC_ALL): string|bool

Source: `wire/modules/LanguageSupport/Language.php`

Get locale for this language

See the `Languages::getLocale()` method for full details.

## Usage

~~~~~
// basic usage
$string = $language->getLocale();

// usage with all arguments
$string = $language->getLocale($category = LC_ALL);
~~~~~

## Arguments

- `$category` (optional) `int` Optional category (default=LC_ALL)

## Return value

- `string|bool`

## See Also

- [Languages::setLocale()](../Languages/method-setlocale.md)
