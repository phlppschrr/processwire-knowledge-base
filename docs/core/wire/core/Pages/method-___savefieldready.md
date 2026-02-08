# $pages->saveFieldReady(Page $page, Field $field)

Source: `wire/core/Pages.php`

Hook called when Pages::saveField is ready to execute

## Usage

~~~~~
// basic usage
$result = $pages->saveFieldReady($page, $field);

// usage with all arguments
$result = $pages->saveFieldReady(Page $page, Field $field);
~~~~~

## Hookable

- Hookable method name: `saveFieldReady`
- Implementation: `___saveFieldReady`
- Hook with: `$pages->saveFieldReady()`

## Arguments

- `$page` `Page`
- `$field` `Field`

## See Also

- [Pages::savePageOrFieldReady()](method-___savepageorfieldready.md)
