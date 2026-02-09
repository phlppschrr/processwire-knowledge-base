# Users: other

Source: `wire/core/Users.php`

- find($selector): PageArray Return the User(s) matching the the given selector query.

- add($name): User Add new User with the given name and return it.

- [save($user): bool](method-___save.md) Save given User.

- delete($user): bool Delete the given User.

- [saveReady($user): array](method-___saveready.md) Hook called just before a User is saved

- saved($user, array $changes): void Hook called after a User has been saved

- added($user): void Hook called just after a User is added

- deleteReady($user): void Hook called before a User is deleted

- deleted($user): void Hook called after a User is deleted

- new($options = []): User Create new User instance in memory (3.0.249+)
