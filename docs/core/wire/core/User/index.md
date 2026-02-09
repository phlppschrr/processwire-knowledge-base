# User

Source: `wire/core/User.php`

Inherits: `Page`


Groups:
Group: [access](group-access.md)
Group: [common](group-common.md)
Group: [languages](group-languages.md)
Group: [other](group-other.md)

ProcessWire UserPage

A type of Page used for storing an individual User


The $user API variable is a type of page representing the current user, and the User class is Page type used for all users.

@link http://processwire.com/api/variables/user/ Offical $user API variable Documentation



Additional notes regarding the $user->pass property:
Note that when getting, this returns a hashed version of the password, so it is not typically useful to get this property.
However, it is useful to set this property if you want to change the password. When you change a password, it is assumed
to be the non-hashed/non-encrypted version. ProcessWire will hash it automatically when the user is saved.

Methods:
- [`__construct(?Template $tpl = null)`](method-__construct.md)
- [`hasRole(string|Role|int $role): bool`](method-hasrole.md)
- [`addRole(string|int|Role $role): bool`](method-addrole.md)
- [`removeRole(string|int|Role $role): bool`](method-removerole.md)
- [`hasPermission(string|Permission $name, Page|Template|bool|string $context = null): bool|array`](method-haspermission.md)
- [`hasPagePermission($name, ?Page $page = null): bool`](method-___haspagepermission.md) (hookable)
- [`hasTemplatePermission(string|Permission $name, Template|int|string $template): bool`](method-___hastemplatepermission.md) (hookable)
- [`getPermissions(?Page $page = null): PageArray`](method-getpermissions.md)
- [`isSuperuser(): bool`](method-issuperuser.md)
- [`isGuest(): bool`](method-isguest.md)
- [`isLoggedin(): bool`](method-isloggedin.md)
- [`setLanguage(Language|string|int $language): self`](method-setlanguage.md)
- [`get(string $key): null|mixed`](method-get.md)
- [`hasTfa(bool $getInstance = false): bool|string|Tfa`](method-hastfa.md)
