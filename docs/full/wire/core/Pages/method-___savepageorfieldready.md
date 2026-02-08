# $pages->___savePageOrFieldReady(Page $page, $fieldName = '')

Source: `wire/core/Pages.php`

Hook called when either of Pages::save or Pages::saveField is ready to execute

## Arguments

- `$page` `Page`
- `$fieldName` (optional) `string` Populated only if call originates from saveField

## See also

- [Pages::saveReady()](method-___saveready.md)
- [Pages::saveFieldReady()](method-___savefieldready.md)
