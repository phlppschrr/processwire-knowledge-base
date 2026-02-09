# WireInputData

Source: `wire/core/WireInputData.php`

Inherits: `Wire`
Implements: `ArrayAccess`, `IteratorAggregate`, `Countable`


Groups:
Group: [other](group-other.md)

WireInputData manages one of GET, POST, COOKIE, or whitelist

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

Methods:
- [`__construct(array &$input = array(), bool $lazy = false)`](method-__construct.md)
- [`setArray(array $input): $this`](method-setarray.md)
- [`getArray(): array`](method-getarray.md)
- [`__set(string $key, mixed $value)`](method-__set.md)
- [`set(string $key, string|int|float|array|null $value, array|int|string $options = array()): $this`](method-set.md)
- [`get(string $key, array|int|string $options = array()): string|int|float|array|null`](method-get.md)
- [`findOne(string $pattern, array|int|string $options = array()): string|int|float|array|null`](method-findone.md)
- [`find(string $pattern, array $options = array()): array`](method-find.md)
- [`cleanArray(array $a): array`](method-cleanarray.md)
- [`setStripSlashes($stripSlashes)`](method-setstripslashes.md)
- [`__get(string $key): mixed|null`](method-__get.md)
- [`remove(string $key): $this`](method-remove.md)
- [`removeAll(): $this`](method-removeall.md)
- [`callUnknown(string $method, array $arguments): string|int|array|float|null`](method-___callunknown.md) (hookable)
