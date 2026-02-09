# Roles

Source: `wire/core/Roles.php`

Inherits: `PagesType`


Groups:
Group: [other](group-other.md)

The Roles class serves as the $roles API variable.

Provides management of all Role pages for access control.

Methods:
- [`get(string $selectorString): Role|NullPage|null`](method-get.md)
- [`save(Page $page): bool`](method-___save.md) (hookable)
- [`delete(Page $page, bool $recursive = false): bool`](method-___delete.md) (hookable)
- [`add(string $name): Role|NullPage`](method-___add.md) (hookable)
