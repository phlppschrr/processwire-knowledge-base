# Permissions

Source: `wire/core/Permissions.php`

Inherits: `PagesType`

## Summary

The Permissions class serves as the `$permissions` API variable.

Common methods:
- [`has()`](method-has.md)
- [`getPermissionNameIds()`](method-getpermissionnameids.md)
- [`save()`](method-___save.md)
- [`delete()`](method-___delete.md)
- [`add()`](method-___add.md)

Groups:
Group: [other](group-other.md)

Provides management of all Permission pages independent of users, for access control.

## Methods
- [`has(string $name): bool`](method-has.md) Does the system have a permission with the given name?
- [`save(Page $page): bool`](method-___save.md) (hookable) Save a Permission
- [`delete(Page $page, bool $recursive = false): bool`](method-___delete.md) (hookable) Permanently delete a Permission
- [`add(string $name): Permission|NullPage`](method-___add.md) (hookable) Add a new Permission with the given name and return it
- [`getReducerPermissions(): array`](method-getreducerpermissions.md) Get permission names that can reduce existing access, when installed
- [`getIterator(): array|PageArray|\Traversable`](method-getiterator.md) Returns all installed Permission pages and enables foreach() iteration of $permissions
- [`saved(Page $page, array $changes = array(), array $values = array())`](method-___saved.md) (hookable) Hook called when a permission is saved
- [`deleted(Page $page)`](method-___deleted.md) (hookable) Hook called when a permission is deleted
