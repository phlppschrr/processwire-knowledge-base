# $roles->delete(Page $page, $recursive = false): bool

Source: `wire/core/Roles.php`

Permanently delete a Role

## Usage

~~~~~
// basic usage
$bool = $roles->delete($page);

// usage with all arguments
$bool = $roles->delete(Page $page, $recursive = false);
~~~~~

## Hookable

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `$roles->delete()`

## Arguments

- `$page` `Role|Page` Permission to delete
- `$recursive` (optional) `bool` If set to true, then this will attempt to delete any pages below the Permission too.

## Return value

- `bool` True on success, false on failure

## Exceptions

- `WireException`
