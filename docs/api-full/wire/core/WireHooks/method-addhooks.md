# $wireHooks->addHooks(Wire $object, $methods, $toObject, $toMethod = null, $options = array()): string

Source: `wire/core/WireHooks.php`

Add a hooks to multiple methods at once

This is the same as addHook() except that the $method argument is an array or CSV string of hook definitions.
See the addHook() method for more detailed info on arguments.

## Usage

~~~~~
// basic usage
$string = $wireHooks->addHooks($object, $methods, $toObject);

// usage with all arguments
$string = $wireHooks->addHooks(Wire $object, $methods, $toObject, $toMethod = null, $options = array());
~~~~~

## Arguments

- `$object` `Wire`
- `$methods` `array|string` Array of one or more strings hook definitions, or CSV string of hook definitions
- `$toObject` `object|null|callable`
- `$toMethod` (optional) `string|array|null`
- `$options` (optional) `array`

## Return value

- `string` CSV string of hook IDs that were added

## Exceptions

- `WireException`

## Since

3.0.137
