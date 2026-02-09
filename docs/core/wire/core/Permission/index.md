# Permission

Source: `wire/core/Permission.php`

ProcessWire Permission Page

Permission is a Page type used for storing an individual permission.
One or more Permission objects are attached to `Role` objects, which are then attached to `User` objects
and `Template` objects, forming ProcessWire's role-based access control system. Outside of roles,
Permission objects are managed with the `$permissions` API variable.

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [wired()](method-wired.md)
