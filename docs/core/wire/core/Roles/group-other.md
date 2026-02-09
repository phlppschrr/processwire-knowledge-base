# Roles: other

Source: `wire/core/Roles.php`

- find($selector): PageArray Return the Role(s) matching the the given selector.

- [add($name): Role](method-___add.md) Add new Role with the given name and return it.

- [save(Role $role): bool](method-___save.md) Save given role.

- [delete(Role $role): bool](method-___delete.md) Delete the given role.

- saveReady(Page $page): array Hook called just before a Role is saved

- saved(Page $page, array $changes = [], $values = []): void Hook called after a role has been saved

- added(Page $page): void Hook called just after a Role is added

- deleteReady(Page $page): void Hook called before a Role is deleted

- deleted(Page $page): void Hook called after a Role is deleted

- new($options = []): Role Create new Role instance in memory (3.0.249+)
