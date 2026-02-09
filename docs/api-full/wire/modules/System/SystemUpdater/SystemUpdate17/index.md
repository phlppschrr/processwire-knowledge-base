# SystemUpdate17

Source: `wire/modules/System/SystemUpdater/SystemUpdate17.php`

Inherits: `SystemUpdate`

Apply secondary layer of .htaccess protections for various site directories
as a fallback in case root .htaccess ever becomes corrupted or goes missing

Methods:
- [`update(): bool`](method-update.md) Apply the update
- [`isApache(): bool`](method-isapache.md) Are we running under Apache?
- [`isUseful(): bool`](method-isuseful.md) Is this update useful for this installation?
