# $pages->___savePageOrFieldReady(Page $page, $fieldName = '')

Source: `wire/core/Pages.php`

Hook called when either of Pages::save or Pages::saveField is ready to execute

## Usage

~~~~~
// basic usage
$result = $pages->___savePageOrFieldReady($page);

// usage with all arguments
$result = $pages->___savePageOrFieldReady(Page $page, $fieldName = '');
~~~~~

## Arguments

- `$page` `Page`
- `$fieldName` (optional) `string` Populated only if call originates from saveField

## See Also

- [Pages::saveReady()](method-___saveready.md)
- [Pages::saveFieldReady()](method-___savefieldready.md)
