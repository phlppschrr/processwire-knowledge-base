# WireInputData

Source: `wire/core/WireInputData.php`

Inherits: `Wire`
Implements: `ArrayAccess`, `IteratorAggregate`, `Countable`

## Summary

WireInputData manages one of GET, POST, COOKIE, or whitelist

Common methods:
- [`setArray()`](method-setarray.md)
- [`getArray()`](method-getarray.md)
- [`set()`](method-set.md)
- [`get()`](method-get.md)
- [`findOne()`](method-findone.md)

Groups:
Group: [other](group-other.md)

WireInputData and the WireInput class together form a simple
front end to PHP's $_GET, $_POST, and $_COOKIE superglobals.

Vars retrieved from here will not have to consider magic_quotes.
No sanitization or filtering is done, other than disallowing
multi-dimensional arrays in input.

WireInputData specifically manages one of: get, post, cookie or
whitelist, whereas the WireInput class provides access to the 3
InputData instances.

Each WireInputData is not instantiated unless specifically asked for.


@link http://processwire.com/api/ref/input/ Offical $input API variable documentation

## Methods
- [`__construct(array &$input = array(), bool $lazy = false)`](method-__construct.md) Construct
- [`setArray(array $input): $this`](method-setarray.md) Set associative array of variables to store
- [`getArray(): array`](method-getarray.md) Get associative array of all input variables
- [`__set(string $key, mixed $value)`](method-__set.md) Set an input value
- [`set(string $key, string|int|float|array|null $value, array|int|string $options = array()): $this`](method-set.md) Set a value
- [`get(string $key, array|int|string $options = array()): string|int|float|array|null`](method-get.md) Get a value
- [`findOne(string $pattern, array|int|string $options = array()): string|int|float|array|null`](method-findone.md) Find one input var that matches given pattern in name (or optionally value)
- [`find(string $pattern, array $options = array()): array`](method-find.md) Find all input vars that match given pattern in name (or optionally value)
- [`cleanArray(array $a): array`](method-cleanarray.md) Clean an array of data
- [`setStripSlashes($stripSlashes)`](method-setstripslashes.md) Set whether or not slashes should be stripped
- [`__get(string $key): mixed|null`](method-__get.md) Get an input value
- [`remove(string $key): $this`](method-remove.md) Remove a value from input
- [`removeAll(): $this`](method-removeall.md) Remove all values from input
- [`callUnknown(string $method, array $arguments): string|int|array|float|null`](method-___callunknown.md) (hookable) Maps to Sanitizer functions
