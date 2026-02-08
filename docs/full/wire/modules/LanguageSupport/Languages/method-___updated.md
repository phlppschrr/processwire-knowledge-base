# $languages->___updated(Page $language, $what)

Source: `wire/modules/LanguageSupport/Languages.php`

Hook called when a language is added or deleted

## Usage

~~~~~
// basic usage
$result = $languages->___updated($language, $what);

// usage with all arguments
$result = $languages->___updated(Page $language, $what);
~~~~~

## Arguments

- `$language` `Page`
- `$what` `string` What occurred? ('added' or 'deleted')
