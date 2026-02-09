# Users: other

Source: `wire/core/Users.php`

- [`find($selector): PageArray`](method-find.md) Return the `User(s)` matching the the given selector query.
- [`add($name): User`](method-add.md) Add new User with the given name and return it.
- [`save($user): bool`](method-___save.md) Save given User.
- [`delete($user): bool`](method-delete.md) Delete the given User.
- [`saveReady($user): array`](method-___saveready.md) Hook called just before a User is saved
- [`saved($user, array $changes): void`](method-saved.md) Hook called after a User has been saved
- [`added($user): void`](method-added.md) Hook called just after a User is added
- [`deleteReady($user): void`](method-deleteready.md) Hook called before a User is deleted
- [`deleted($user): void`](method-deleted.md) Hook called after a User is deleted
- [`new($options = []): User`](method-new.md) Create new User instance in memory (3.0.249+)
