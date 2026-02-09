# WireFuelable

Source: `wire/core/Interfaces.php`

## Summary

Interface that indicates a class supports API variable dependency injection and retrieval

Common methods:
- [`wire()`](method-wire.md)
- [`setWire()`](method-setwire.md)
- [`getWire()`](method-getwire.md)

## Methods
- [`wire(string|WireFuelable $name = '', null|mixed $value = null, bool $lock = false): mixed|Fuel`](method-wire.md) Get or inject a ProcessWire API variable or fuel a new object instance
- [`setWire(ProcessWire $wire)`](method-setwire.md) Set the ProcessWire instance
- [`getWire(): ProcessWire`](method-getwire.md) Get the ProcessWire instance
