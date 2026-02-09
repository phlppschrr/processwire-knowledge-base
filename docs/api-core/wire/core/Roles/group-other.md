# Roles: other

Source: `wire/core/Roles.php`

- [`find($selector): PageArray`](method-find.md) Return the `Role(s)` matching the the given selector.
- [`add($name): Role`](method-___add.md) Add new Role with the given name and return it.
- [`save(Role $role): bool`](method-___save.md) Save given role.
- [`delete(Role $role): bool`](method-___delete.md) Delete the given role.
- [`saveReady(Page $page): array`](method-saveready.md) Hook called just before a Role is saved
- [`saved(Page $page, array $changes = [], $values = []): void`](method-saved.md) Hook called after a role has been saved
- [`added(Page $page): void`](method-added.md) Hook called just after a Role is added
- [`deleteReady(Page $page): void`](method-deleteready.md) Hook called before a Role is deleted
- `deleted(Page $page): void` Hook called after a Role is deleted
- [`new($options = []): Role`](method-new.md) Create new Role instance in memory (3.0.249+)
