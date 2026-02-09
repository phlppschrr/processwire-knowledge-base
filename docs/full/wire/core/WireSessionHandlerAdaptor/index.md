# WireSessionHandlerAdaptor

Source: `wire/core/WireSessionHandlerAdaptor.php`

Implements: `SessionHandlerInterface`

Adaptor between WireSessionHandler modules and PHP’s SessionHandlerInterface

Used on PHP 8.4+ installations only. Necessary because:

- PHP's SessionHandlerInterface in PHP 8.5+ is not compatible with ProcessWire’s
  WireSessionHandler module type primarily because of declared union return types
  in the SessionHandlerInterface.

- There are already other WireSessionHandler modules in existance that would require
  changes without this adaptor.

- PHP 8.4+ has deprecated setting the save handler method-by-method and instead requires
  a class that implements SessionHandlerInterface. So this is that class.

 - This adaptor will work on any PHP 8.x version but we use it just for PHP 8.4+ currently.

@since 3.0.255

Methods:
- [`__construct(WireSessionHandler $handler)`](method-__construct.md)
- [`close(): bool`](method-close.md)
- [`destroy(string $id): bool`](method-destroy.md)
- [`gc(int $max_lifetime): int|false`](method-gc.md)
- [`open(string $path, string $name): bool`](method-open.md)
- [`read(string $id): string|false`](method-read.md)
- [`write(string $id, string $data): bool`](method-write.md)
