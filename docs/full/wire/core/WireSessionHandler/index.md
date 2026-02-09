# WireSessionHandler

Source: `wire/core/WireSessionHandler.php`

Inherits: `WireData`
Implements: `Module`

ProcessWire Session Handler

This is an abstract class for a session handler module to extend from.
It provides the interface and some basic functions. For an example, see:
It provides the interface and some basic functions. For an example, see:
/wire/modules/Session/SessionHandlerDB/SessionHandlerDB.module

Methods:
- [`wired()`](method-wired.md)
- [`init()`](method-init.md)
- [`hookSessionInit(HookEvent $event)`](method-hooksessioninit.md)
- [`attach()`](method-attach.md)
- [`open(string $path, string $name): bool`](method-open.md)
- [`close(): bool`](method-close.md)
- [`read(string $id): string|false`](method-read.md)
- [`write(string $id, $data): bool`](method-write.md)
- [`destroy(string $id): bool`](method-destroy.md)
- [`gc(int $seconds): bool`](method-gc.md)
- [`sessionExists(): bool`](method-sessionexists.md)
- [`isSingular()`](method-issingular.md)
- [`isAutoload()`](method-isautoload.md)
