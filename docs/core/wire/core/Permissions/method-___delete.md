# $permissions->delete(Page $page, $recursive = false): bool

Source: `wire/core/Permissions.php`

Permanently delete a Permission

## Usage

~~~~~
// basic usage
$bool = $permissions->delete($page);

// usage with all arguments
$bool = $permissions->delete(Page $page, $recursive = false);
~~~~~

## Hookable

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `$permissions->delete()`

## Arguments

- `$page` `Permission|Page` Permission to delete
- `$recursive` (optional) `bool` If set to true, then this will attempt to delete any pages below the Permission too.

## Return value

- `bool` True on success, false on failure

## Exceptions

- `WireException`
