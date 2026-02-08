# $permissions->deleted(Page $page)

Source: `wire/core/Permissions.php`

Hook called when a permission is deleted

## Usage

~~~~~
// basic usage
$result = $permissions->deleted($page);

// usage with all arguments
$result = $permissions->deleted(Page $page);
~~~~~

## Hookable

- Hookable method name: `deleted`
- Implementation: `___deleted`
- Hook with: `$permissions->deleted()`

## Arguments

- `$page` `Page` Page that was deleted

## Exceptions

- `WireException`
