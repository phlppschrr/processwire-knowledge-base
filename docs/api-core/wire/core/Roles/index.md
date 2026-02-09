# Roles

Source: `wire/core/Roles.php`

Inherits: `PagesType`

## Summary

The Roles class serves as the `$roles` API variable.

Common methods:
- [`getGuestRole()`](method-getguestrole.md)
- [`get()`](method-get.md)
- [`save()`](method-___save.md)
- [`delete()`](method-___delete.md)
- [`add()`](method-___add.md)

Groups:
Group: [other](group-other.md)

Provides management of all Role pages for access control.

## Methods
- [`get(string $selectorString): Role|NullPage|null`](method-get.md) Get a Role by name, numeric ID or selector
- [`save(Page $page): bool`](method-___save.md) (hookable) Save a Role
- [`delete(Page $page, bool $recursive = false): bool`](method-___delete.md) (hookable) Permanently delete a Role
- [`add(string $name): Role|NullPage`](method-___add.md) (hookable) Add a new Role with the given name and return it
