# WireData

Source: `wire/core/WireData.php`

Inherits: `Wire`
Implements: `IteratorAggregate`, `ArrayAccess`

## Summary

ProcessWire WireData

Common methods:
- [`set()`](method-set.md)
- [`setQuietly()`](method-setquietly.md)
- [`isEqual()`](method-isequal.md)
- [`setArray()`](method-setarray.md)
- [`get()`](method-get.md)

Groups:
Group: [other](group-other.md)

This is the base data container class used throughout ProcessWire.
It provides get and set access to properties internally stored in a `$data` array.
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

## Methods
- [`set(string $key, mixed $value): $this`](method-set.md) Set a value to this object’s data
- [`setQuietly(string $key, mixed $value): $this`](method-setquietly.md) Same as set() but without change tracking
- [`setArray(array $data): $this`](method-setarray.md) Set an array of key=value pairs
- [`__set(string $key, mixed $value)`](method-__set.md) Provides direct reference access to set values in the `$data` array
- [`get(string|object $key): mixed|null`](method-get.md) Retrieve the value for a previously set property, or retrieve an API variable
- [`data(string|array $key = null, mixed $value = null): array|WireData|null`](method-data.md) Get or set a low-level data value
- [`getArray(): array`](method-getarray.md) Returns the full array of properties set to this object
- [`getDot(string $key): null|mixed`](method-getdot.md) Get a property via dot syntax: field.subfield.subfield
- [`__get(string $name): mixed|null`](method-__get.md) Provides direct reference access to variables in the `$data` array
- [`__invoke(string $key): mixed`](method-__invoke.md) Enables use of `$var`('key')
- [`remove(string $key): $this`](method-remove.md) Remove a previously set property
- [`getIterator(): \ArrayObject`](method-getiterator.md) Enables the object data properties to be iterable as an array
- [`has(string $key): bool`](method-has.md) Does this object have the given property?
- [`and(WireArray|WireData|string|null $items = null): WireArray`](method-___and.md) (hookable) Take the current item and append the given item(s), returning a new WireArray
- [`__debugInfo(): array`](method-__debuginfo.md) debugInfo PHP 5.6+ magic method
