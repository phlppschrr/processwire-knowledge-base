# Permissions: other

Source: `wire/core/Permissions.php`

- [find($selector): PageArray](method-find.md) Return the permissions(s) matching the the given selector query.
- [get($selector): Permission|NullPage](method-get.md) Return permission by given name, numeric ID or a selector string.
- [saveReady(Page $page): array](method-saveready.md) Hook called just before a Permission is saved
- [saved(Page $page, array $changes = array(), $values = []): void](method-___saved.md)
- [added(Page $page): void](method-added.md) Hook called just after a Permission is added
- [deleteReady(Page $page): void](method-deleteready.md) Hook called before a Permission is deleted
- [deleted(Page $page): void](method-___deleted.md) Hook called after a permission is deleted
- [new($options = []): Permission](method-new.md) Create new Permission instance in memory (3.0.249+)
