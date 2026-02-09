# ModulesClass

Source: `wire/core/ModulesClass.php`

Inherits: `Wire`

## Summary

ProcessWire Modules: Class

Common methods:
- [`moduleID()`](method-moduleid.md)
- [`moduleName()`](method-modulename.md)
- [`log()`](method-log.md)
- [`error()`](method-error.md)

Base for Modules helper classes.

## Methods
- [`__construct(Modules $modules)`](method-__construct.md) Construct
- [`moduleID(string|int|Module $name): int`](method-moduleid.md) Convert given value to module ID
- [`moduleName(int|string|Module $id): string`](method-modulename.md) Convert given value to module name
- [`log(string $str, array|string $options = array()): WireLog`](method-log.md) Save to the modules log
