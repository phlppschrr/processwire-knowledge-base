# PageAccess

Source: `wire/core/PageAccess.php`

ProcessWire Page Access

Provides implementation for Page access functions.

Methods:
- [`getType(string|int|Permission $name): string`](method-gettype.md)
- [`getAccessParent(Page $page, string $type = 'view', int $level = 0): Page|NullPage`](method-getaccessparent.md)
- [`getAccessTemplate(Page $page, string $type = 'view'): Template|null`](method-getaccesstemplate.md)
- [`getAccessRoles(Page $page, string $type = 'view'): PageArray`](method-getaccessroles.md)
- [`hasAccessRole(Page $page, string|int|Role $role, string $type = 'view'): bool`](method-hasaccessrole.md)
- [`wire(string|WireFuelable $name = '', null|mixed $value = null, bool $lock = false): mixed|Fuel`](method-wire.md)
- [`setWire(ProcessWire $wire)`](method-setwire.md)
- [`getWire(): ProcessWire`](method-getwire.md)
