# Role

Source: `wire/core/Role.php`

Inherits: `Page`


Groups:
Group: [other](group-other.md)

ProcessWire Role Page

Role is a type of Page used for grouping permissions to users.
Any given User will have one or more roles, each with zero or more permissions assigned to it.
Note that most public API-level access checking is typically performed from the User rather than
the Role(s), as it accounts for the combined roles. Please also see `User`, `Permission` and the
access related methods on `Page`.

Methods:
- [`__construct(?Template $tpl = null)`](method-__construct.md)
- [`wired()`](method-wired.md)
- [`getPredefinedTemplate(): Template`](method-getpredefinedtemplate.md)
- [`getPredefinedParent(): Page`](method-getpredefinedparent.md)
- [`hasPermission(string|int|Permission $permission, Page|Template|null $context = null): bool`](method-haspermission.md)
- [`hasPermissionContext(bool $has, Permission $permission, Wire $context): bool`](method-haspermissioncontext.md)
- [`addPermission(string|int|Permission $permission): bool`](method-addpermission.md)
- [`removePermission(string|int|Permission $permission): bool`](method-removepermission.md)
