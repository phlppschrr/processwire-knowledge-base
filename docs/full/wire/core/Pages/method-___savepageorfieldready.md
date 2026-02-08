# $pages->savePageOrFieldReady(Page $page, $fieldName = '')

Source: `wire/core/Pages.php`

Hook called when either of Pages::save or Pages::saveField is ready to execute

## Usage

~~~~~
// basic usage
$result = $pages->savePageOrFieldReady($page);

// usage with all arguments
$result = $pages->savePageOrFieldReady(Page $page, $fieldName = '');
~~~~~

## Hookable

- Hookable method name: `savePageOrFieldReady`
- Implementation: `___savePageOrFieldReady`
- Hook with: `$pages->savePageOrFieldReady()`

## Arguments

- `$page` `Page`
- `$fieldName` (optional) `string` Populated only if call originates from saveField

## See Also

- [Pages::saveReady()](method-___saveready.md)
- [Pages::saveFieldReady()](method-___savefieldready.md)
