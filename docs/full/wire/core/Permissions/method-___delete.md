# $permissions->___delete(Page $page, $recursive = false): bool

Source: `wire/core/Permissions.php`

Permanently delete a Permission

## Arguments

- Permission|Page $page Permission to delete
- bool $recursive If set to true, then this will attempt to delete any pages below the Permission too.

## Return value

bool True on success, false on failure

## Throws

- WireException
