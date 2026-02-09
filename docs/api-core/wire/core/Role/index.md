# Role

Source: `wire/core/Role.php`

Inherits: `Page`

## Summary

ProcessWire Role Page

Common methods:
- [`wired()`](method-wired.md)
- [`getPredefinedTemplate()`](method-getpredefinedtemplate.md)
- [`getPredefinedParent()`](method-getpredefinedparent.md)
- [`hasPermission()`](method-haspermission.md)
- [`hasPermissionContext()`](method-haspermissioncontext.md)

Groups:
Group: [other](group-other.md)

Role is a type of Page used for grouping permissions to users.
Any given User will have one or more roles, each with zero or more permissions assigned to it.
Note that most public API-level access checking is typically performed from the User rather than
the Role(s), as it accounts for the combined roles. Please also see `User`, `Permission` and the
access related methods on `Page`.

## Methods
- [`__construct(?Template $tpl = null)`](method-__construct.md) Create a new Role page in memory.
- [`wired()`](method-wired.md) Wired to API
- [`getPredefinedTemplate(): Template`](method-getpredefinedtemplate.md) Get predefined template (template method)
- [`getPredefinedParent(): Page`](method-getpredefinedparent.md) Get predefined parent page (template method)
- [`hasPermission(string|int|Permission $permission, Page|Template|null $context = null): bool`](method-haspermission.md) Does this role have the given permission name, id or object?
- [`hasPermissionContext(bool $has, Permission $permission, Wire $context): bool`](method-haspermissioncontext.md) Return whether the role has the permission within the context of a Page or Template
- [`addPermission(string|int|Permission $permission): bool`](method-addpermission.md) Add the given Permission string, id or object.
- [`removePermission(string|int|Permission $permission): bool`](method-removepermission.md) Remove the given permission string, id or object.
