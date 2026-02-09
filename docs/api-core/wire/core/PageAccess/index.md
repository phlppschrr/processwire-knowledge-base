# PageAccess

Source: `wire/core/PageAccess.php`

ProcessWire Page Access

Provides implementation for Page access functions.

Methods:
- [`getType(string|int|Permission $name): string`](method-gettype.md) Normalize a permission name type
- [`getAccessParent(Page $page, string $type = 'view', int $level = 0): Page|NullPage`](method-getaccessparent.md) Returns the parent page that has the template from which we get our role/access settings from
- [`getAccessTemplate(Page $page, string $type = 'view'): Template|null`](method-getaccesstemplate.md) Returns the template from which we get our role/access settings from
- [`getAccessRoles(Page $page, string $type = 'view'): PageArray`](method-getaccessroles.md) Return the PageArray of roles that have access to this page
- [`hasAccessRole(Page $page, string|int|Role $role, string $type = 'view'): bool`](method-hasaccessrole.md) Returns whether this page has the given access role
- [`wire(string|WireFuelable $name = '', null|mixed $value = null, bool $lock = false): mixed|Fuel`](method-wire.md) Get or inject a ProcessWire API variable or fuel a new object instance
- [`setWire(ProcessWire $wire)`](method-setwire.md) Set the ProcessWire instance
- [`getWire(): ProcessWire`](method-getwire.md) Get the ProcessWire instance
