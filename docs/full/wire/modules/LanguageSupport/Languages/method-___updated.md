# $languages->updated(Page $language, $what)

Source: `wire/modules/LanguageSupport/Languages.php`

Hook called when a language is added or deleted

## Usage

~~~~~
// basic usage
$result = $languages->updated($language, $what);

// usage with all arguments
$result = $languages->updated(Page $language, $what);
~~~~~

## Hookable

- Hookable method name: `updated`
- Implementation: `___updated`
- Hook with: `$languages->updated()`

## Arguments

- `$language` `Page`
- `$what` `string` What occurred? ('added' or 'deleted')
