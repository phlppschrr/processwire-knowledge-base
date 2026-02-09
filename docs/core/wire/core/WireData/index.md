# WireData

Source: `wire/core/WireData.php`

Inherits: `Wire`
Implements: `IteratorAggregate`, `ArrayAccess`


Groups:
Group: [other](group-other.md)

ProcessWire WireData

This is the base data container class used throughout ProcessWire.
It provides get and set access to properties internally stored in a $data array.
Otherwise it is identical to the Wire class.

WireData is the base data-storage class used by many ProcessWire object types and most modules.
WireData is very much like its parent `Wire` class with the fundamental difference being that it is designed
for runtime data storage. It provides this primarily through the built-in `get()` and `set()` methods for
getting and setting named properties to WireData objects. The most common example of a WireData object is
`Page`, the type used for all pages in ProcessWire.

Properties set to a WireData object can also be set or accessed directly, like `$item->property` or using
array access like `$item[$property]`. If you `foreach()` a WireData object, the default behavior is to
iterate all of the properties/values present within it.

May also be accessed as array.

Methods:
- [`set(string $key, mixed $value): $this`](method-set.md)
- [`setQuietly(string $key, mixed $value): $this`](method-setquietly.md)
- [`setArray(array $data): $this`](method-setarray.md)
- [`__set(string $key, mixed $value)`](method-__set.md)
- [`get(string|object $key): mixed|null`](method-get.md)
- [`data(string|array $key = null, mixed $value = null): array|WireData|null`](method-data.md)
- [`getArray(): array`](method-getarray.md)
- [`getDot(string $key): null|mixed`](method-getdot.md)
- [`__get(string $name): mixed|null`](method-__get.md)
- [`__invoke(string $key): mixed`](method-__invoke.md)
- [`remove(string $key): $this`](method-remove.md)
- [`getIterator(): \ArrayObject`](method-getiterator.md)
- [`has(string $key): bool`](method-has.md)
- [`and(WireArray|WireData|string|null $items = null): WireArray`](method-___and.md) (hookable)
- [`__debugInfo(): array`](method-__debuginfo.md)
