# Permissions: other

Source: `wire/core/Permissions.php`

- find($selector): PageArray Return the permissions(s) matching the the given selector query.

- get($selector): Permission|NullPage Return permission by given name, numeric ID or a selector string.

- saveReady(Page $page): array Hook called just before a Permission is saved

- [saved(Page $page, array $changes = array(): void](method-___saved.md) , $values = [])

- added(Page $page): void Hook called just after a Permission is added

- deleteReady(Page $page): void Hook called before a Permission is deleted

- [deleted(Page $page): void](method-___deleted.md) Hook called after a permission is deleted

- new($options = []): Permission Create new Permission instance in memory (3.0.249+)
