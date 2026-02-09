# Permissions

Source: `wire/core/Permissions.php`

Inherits: `PagesType`


Groups:
Group: [other](group-other.md)

The Permissions class serves as the $permissions API variable.

Provides management of all Permission pages independent of users, for access control.

Methods:
- [`has(string $name): bool`](method-has.md)
- [`save(Page $page): bool`](method-___save.md) (hookable)
- [`delete(Page $page, bool $recursive = false): bool`](method-___delete.md) (hookable)
- [`add(string $name): Permission|NullPage`](method-___add.md) (hookable)
- [`getReducerPermissions(): array`](method-getreducerpermissions.md)
- [`getIterator(): array|PageArray|\Traversable`](method-getiterator.md)
- [`saved(Page $page, array $changes = array(), array $values = array())`](method-___saved.md) (hookable)
- [`deleted(Page $page)`](method-___deleted.md) (hookable)
