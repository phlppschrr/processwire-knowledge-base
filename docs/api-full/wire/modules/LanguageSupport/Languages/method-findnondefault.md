# $languages->findNonDefault($selector = ''): PageArray

Source: `wire/modules/LanguageSupport/Languages.php`

Find and return all languages except default language

## Usage

~~~~~
// basic usage
$items = $languages->findNonDefault();

// usage with all arguments
$items = $languages->findNonDefault($selector = '');
~~~~~

## Arguments

- `$selector` (optional) `string` Optionally filter by a selector string

## Return value

- `PageArray`
