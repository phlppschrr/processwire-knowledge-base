# Role

Source: `wire/core/Role.php`

ProcessWire Role Page

Role is a type of Page used for grouping permissions to users.
Any given User will have one or more roles, each with zero or more permissions assigned to it.
Note that most public API-level access checking is typically performed from the User rather than
the Role(s), as it accounts for the combined roles. Please also see `User`, `Permission` and the
access related methods on `Page`.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [wired()](method-wired.md)
Method: [getPredefinedTemplate()](method-getpredefinedtemplate.md)
Method: [getPredefinedParent()](method-getpredefinedparent.md)
Method: [hasPermission()](method-haspermission.md)
Method: [hasPermissionContext()](method-haspermissioncontext.md)
Method: [addPermission()](method-addpermission.md)
Method: [removePermission()](method-removepermission.md)
