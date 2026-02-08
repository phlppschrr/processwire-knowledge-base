# $wireHooks->addHooks(Wire $object, $methods, $toObject, $toMethod = null, $options = array()): string

Source: `wire/core/WireHooks.php`

Add a hooks to multiple methods at once

This is the same as addHook() except that the $method argument is an array or CSV string of hook definitions.
See the addHook() method for more detailed info on arguments.

## Arguments

- Wire $object
- array|string $methods Array of one or more strings hook definitions, or CSV string of hook definitions
- object|null|callable $toObject
- string|array|null $toMethod
- array $options

## Return value

string CSV string of hook IDs that were added

## Throws

- WireException

## Meta

- @since 3.0.137
