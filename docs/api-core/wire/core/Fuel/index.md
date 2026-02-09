# Fuel

Source: `wire/core/Fuel.php`

Implements: `IteratorAggregate`


Groups:
Group: [other](group-other.md)

ProcessWire Fuel

Fuel maintains a single instance each of multiple objects used throughout the application.
The objects contained in fuel provide access to the ProcessWire API. For instance, $pages,
$users, $fields, and so on. The fuel is required to keep the system running, so to speak.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

Methods:
- [`set(string $key, object|mixed $value, bool $lock = false): $this`](method-set.md)
- [`remove($key): bool`](method-remove.md) Remove an API variable from the Fuel
