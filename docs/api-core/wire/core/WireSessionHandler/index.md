# WireSessionHandler

Source: `wire/core/WireSessionHandler.php`

Inherits: `WireData`
Implements: `Module`

## Summary

ProcessWire Session Handler

Common methods:
- [`wired()`](method-wired.md)
- [`init()`](method-init.md)
- [`hookSessionInit()`](method-hooksessioninit.md)
- [`attach()`](method-attach.md)
- [`open()`](method-open.md)

This is an abstract class for a session handler module to extend from.
It provides the interface and some basic functions. For an example, see:
It provides the interface and some basic functions. For an example, see:
/wire/modules/Session/SessionHandlerDB/SessionHandlerDB.module

## Methods
- [`wired()`](method-wired.md) Initialize the save handler when `$modules` sets the current instance
- [`init()`](method-init.md) Initailize, called when module configuration has been populated
- [`hookSessionInit(HookEvent $event)`](method-hooksessioninit.md) Hook before Session::init
- [`attach()`](method-attach.md) Attach this as the session handler
- [`open(string $path, string $name): bool`](method-open.md) Open the session
- [`close(): bool`](method-close.md) Close the session
- [`read(string $id): string|false`](method-read.md) Read and return data for session indicated by `$id`
- [`write(string $id, $data): bool`](method-write.md) Write the given `$data` for the given session ID
- [`destroy(string $id): bool`](method-destroy.md) Destroy the session indicated by the given session ID
- [`gc(int $seconds): bool`](method-gc.md) Garbage collection: remove stale sessions
- [`sessionExists(): bool`](method-sessionexists.md) Does a session currently exist? (i.e. already one started)
- [`isSingular()`](method-issingular.md) Tells the Modules API to only instantiate one instance of this module
- [`isAutoload()`](method-isautoload.md) Tells the Modules API to automatically load this module at boot
