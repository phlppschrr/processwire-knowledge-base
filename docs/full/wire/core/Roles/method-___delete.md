# $roles->___delete(Page $page, $recursive = false): bool

Source: `wire/core/Roles.php`

Permanently delete a Role

## Arguments

- `$page` `Role|Page` Permission to delete
- `$recursive` (optional) `bool` If set to true, then this will attempt to delete any pages below the Permission too.

## Return value

bool True on success, false on failure

## Throws

- WireException
