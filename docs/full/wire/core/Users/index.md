# Users

Source: `wire/core/Users.php`

Inherits: `PagesType`


Groups:
Group: [other](group-other.md)

The Users class serves as the $users API variable.

Manages all users (User objects) in ProcessWire.

Methods:
- [`__construct(ProcessWire $wire, array $templates = array(), array $parents = array())`](method-__construct.md)
- [`get(string $selectorString): User|NullPage|null`](method-get.md)
- [`setCurrentUser(User $user)`](method-setcurrentuser.md)
- [`loaded(Page $page)`](method-loaded.md)
- [`checkGuestRole(User $user)`](method-checkguestrole.md)
- [`getCurrentUser(): User`](method-getcurrentuser.md)
- [`getGuestUser(): User`](method-getguestuser.md)
- [`setAdminThemeByRole(AdminTheme|string $adminTheme, Role $role): int`](method-setadminthemebyrole.md)
- [`save(Page $page): bool`](method-___save.md) (hookable)
- [`saveReady(Page $page): array`](method-___saveready.md) (hookable)
