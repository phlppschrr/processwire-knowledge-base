# Users

Source: `wire/core/Users.php`

Inherits: `PagesType`

## Summary

The Users class serves as the `$users` API variable.

Common methods:
- [`get()`](method-get.md)
- [`setCurrentUser()`](method-setcurrentuser.md)
- [`loaded()`](method-loaded.md)
- [`checkGuestRole()`](method-checkguestrole.md)
- [`getCurrentUser()`](method-getcurrentuser.md)

Groups:
Group: [other](group-other.md)

Manages all users (User objects) in ProcessWire.

## Methods
- [`__construct(ProcessWire $wire, array $templates = array(), array $parents = array())`](method-__construct.md) Construct
- [`get(string $selectorString): User|NullPage|null`](method-get.md) Get the user by name, ID or selector string
- [`setCurrentUser(User $user)`](method-setcurrentuser.md) Set the current system user (the $user API variable)
- [`loaded(Page $page)`](method-loaded.md) Ensure that every user loaded has at least the 'guest' role
- [`checkGuestRole(User $user)`](method-checkguestrole.md) Check that given user has guest role and add it if not
- [`getCurrentUser(): User`](method-getcurrentuser.md) Returns the current user object
- [`getGuestUser(): User`](method-getguestuser.md) Get the 'guest' user account
- [`setAdminThemeByRole(AdminTheme|string $adminTheme, Role $role): int`](method-setadminthemebyrole.md) Set admin theme for all users having role
- [`save(Page $page): bool`](method-___save.md) (hookable) Save a User
- [`saveReady(Page $page): array`](method-___saveready.md) (hookable) Hook called just before a user is saved
