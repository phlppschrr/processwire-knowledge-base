# User

Source: `wire/core/User.php`

Inherits: `Page`

## Summary

ProcessWire UserPage

Common methods:
- [`wired()`](method-wired.md)
- [`hasRole()`](method-hasrole.md)
- [`addRole()`](method-addrole.md)
- [`removeRole()`](method-removerole.md)
- [`hasPermission()`](method-haspermission.md)

Groups:
Group: [access](group-access.md)
Group: [common](group-common.md)
Group: [languages](group-languages.md)
Group: [other](group-other.md)

A type of Page used for storing an individual User


The $user API variable is a type of page representing the current user, and the User class is Page type used for all users.

@link http://processwire.com/api/variables/user/ Offical $user API variable Documentation



Additional notes regarding the $user->pass property:
Note that when getting, this returns a hashed version of the password, so it is not typically useful to get this property.
However, it is useful to set this property if you want to change the password. When you change a password, it is assumed
to be the non-hashed/non-encrypted version. ProcessWire will hash it automatically when the user is saved.

## Methods
- [`__construct(?Template $tpl = null)`](method-__construct.md) Create a new User page in memory.
- [`hasRole(string|Role|int $role): bool`](method-hasrole.md) Does this user have the given Role?
- [`addRole(string|int|Role $role): bool`](method-addrole.md) Add Role to this user
- [`removeRole(string|int|Role $role): bool`](method-removerole.md) Remove Role from this user
- [`hasPermission(string|Permission $name, Page|Template|bool|string $context = null): bool|array`](method-haspermission.md) Does the user have the given permission?
- [`hasPagePermission($name, ?Page $page = null): bool`](method-___haspagepermission.md) (hookable) Does this user have named permission for the given Page?
- [`hasTemplatePermission(string|Permission $name, Template|int|string $template): bool`](method-___hastemplatepermission.md) (hookable) Does this user have the given permission on the given template?
- [`getPermissions(?Page $page = null): PageArray`](method-getpermissions.md) Get this user’s permissions, optionally within the context of a Page.
- [`isSuperuser(): bool`](method-issuperuser.md) Does this user have the superuser role?
- [`isGuest(): bool`](method-isguest.md) Is this the non-logged in guest user?
- [`isLoggedin(): bool`](method-isloggedin.md) Is the current $user logged in and the same as this user?
- [`setLanguage(Language|string|int $language): self`](method-setlanguage.md) Set language for user (quietly)
- [`get(string $key): null|mixed`](method-get.md) Get value
- [`hasTfa(bool $getInstance = false): bool|string|Tfa`](method-hastfa.md) Does user have two-factor authentication (Tfa) enabled? (and what type?)
